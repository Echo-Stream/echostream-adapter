"""Lambda function to inject messages into an Echostream Tenant"""

import json
from logging import INFO, WARNING, getLogger
from os import environ
from typing import Any

from echostream_node import Message
from echostream_node.threading import LambdaEvent, LambdaNode

getLogger().setLevel(environ.get("LOG_LEVEL") or INFO)
getLogger("boto3").setLevel(WARNING)
getLogger("botocore").setLevel(WARNING)

INJECTOR_NODE = LambdaNode()


def handler(event: LambdaEvent, _: Any) -> None:
    """Lambda Function Entry Point"""
    messages: list[Message] = None
    match event:
        case {"Records": [{"EventSource": "aws:sns"}, *_]}:
            """SNS Event"""
            messages = [
                INJECTOR_NODE.create_message(record["Sns"]["Message"])
                for record in event["Records"]
            ]
        case {"Records": [{"eventSource": "aws:sqs"}, *_]}:
            """SQS Event"""
            messages = [
                INJECTOR_NODE.create_message(record["body"])
                for record in event["Records"]
            ]
        case _:
            """Direct Invocation"""
            messages = [
                INJECTOR_NODE.create_message(json.dumps(event, separators=(",", ":")))
            ]
    INJECTOR_NODE.send_messages(messages)
    INJECTOR_NODE.audit_messages(messages)

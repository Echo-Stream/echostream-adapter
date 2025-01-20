# echostream-injector
A lambda function that accepts direct invocation, SQS or SNS and sends the payload into an EchoStream tenant

EchoStream currently has the [echostream-node](https://github.com/Echo-Stream/echostream-node) package for those that work in Python to send messages into an EchoStream tenant.

For those that don't use Python, this adapter make is simple to set up an AWS Lambda function that can receive message payloads from:
- Direct invocation - perhaps the simplest way. Just call the adapter directly, passing the exact payload that you want to be injected into EchoStream.
- SQS - Simply attach one or more SQS Queues as triggers to this Lambda function. All messages sent via those queues will be injected into EchoStream.
- SNS - Simply attach one or more subscriptions as triggers to this Lambda function. All messages sent via those subscriptions will be injected into EchoStream.

> Note - you can impliment all three of the above methods at the same time.

This Lambda function is intended to be deployed as a container. You can, however, build it as a zipfile and deploy it that way.

When deployed into an EchoStream tenant it is strongly recommended that you use a [Cross Account App](https://docs.echo.stream/docs/cross-account-app) to do so.

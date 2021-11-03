# serverless-edc2021
Serverless framework demo for edc2021

[![Serverless Application Framework AWS Lambda API Gateway](https://s3.amazonaws.com/assets.github.serverless/readme-serverless-framework.gif)](https://serverless.com)

**The serverless Framework** Building applications on cloud services. It is a command-line tool that uses easy and approachable YAML syntax to deploy both code and cloud infrastructure needed to make serverless applications.
It is a multi-language framework that supports Node.js, Typescript, Python, Go, Java and more. 

Two demo projects are made in this repos to show the usage of serverless framework on AWS and Azure.

## Prerequisites
1. Azure subscription
2. AWS account credentials.
3. Node.js 8.x or above
4. Requires the use of [direnv](https://direnv.net).
5. VSCODE or PyCharm.

## Quick start

This section applies for both examples on Azure and AWS.

### Install serverless

```
npm install -g serverless
```

### Available templates

```shell
serverless create --help

```

### Deploy service
```shell
serverlss deploy
```

### Invoke the function localy
```shell
serverless invoke local -f <function-name> -l
```

### Remove the service
```shell
serverless remove
```

## Acknowledgement

Thanks for all the participants.

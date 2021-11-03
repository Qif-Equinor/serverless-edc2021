import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def hello(event, context):

    logger.info(f"AWS Lambda processing message from GitHub: {event}.")

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

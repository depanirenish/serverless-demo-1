import json


def hello(event, context):
    body = {
        "message": "This is github action!!-2",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

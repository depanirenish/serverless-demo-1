import json


def hello(event, context):
    body = {
        "message": "This is github action!!-5",
        "custom_heading": "this is value of custom heading",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

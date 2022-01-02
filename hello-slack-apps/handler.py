import json
from base64 import b64decode
from urllib.parse import parse_qs


def parse_event_body(event: dict) -> dict:
    body = b64decode(event['body']).decode()
    qs = parse_qs(body)
    return qs


def parse_args(args: str) -> (str, str):
    elements = args.strip().split()
    if len(elements) < 2:
        raise ValueError("Two args are required: <animal> <message>")
    animal, rest = elements[0], elements[1:]
    rest = " ".join(rest)
    return animal, rest


def hello(event, context):
    print(json.dumps(event))

    response = {"statusCode": 200, "body": ""}
    return response

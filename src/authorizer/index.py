import json


def handler(event, context):
    res = {"isAuthorized": False}
    if event["headers"]["hogeauthorization"] == "hogehoge":
        res.update({"isAuthorized": True, "context": {"hogeKey": 12345}})
    return res

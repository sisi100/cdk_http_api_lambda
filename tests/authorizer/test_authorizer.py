import src.authorizer.index as app


def build_apigw_event(token):
    return {
        "headers": {"hogeauthorization": token},
    }


def test_success():

    event = build_apigw_event("hogehoge")
    ret = app.handler(event, "")
    assert ret["isAuthorized"]


def test_fails():

    event = build_apigw_event("fugafuga")
    ret = app.handler(event, "")
    assert not ret["isAuthorized"]

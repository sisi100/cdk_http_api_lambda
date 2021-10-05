import src.app.index as app


def test_handler():
    event = {}
    ret = app.handler(event, "")
    assert ret["statusCode"] == "200"
    assert ret["body"] == "Hello World !!"

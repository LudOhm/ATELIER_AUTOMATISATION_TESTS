def test_status(resp):
    return resp["status_code"] == 200

def test_json(resp):
    return isinstance(resp["json"], dict)

def test_has_name(resp):
    return "name" in resp["json"]

def test_has_age(resp):
    return "age" in resp["json"] and isinstance(resp["json"]["age"], int)
from tester.client import api_get


def test_status_code():
    r = api_get({"name": "michael"})
    return r["status_code"] == 200


def test_json_exists():
    r = api_get({"name": "michael"})
    return isinstance(r["json"], dict)


def test_name_field():
    r = api_get({"name": "michael"})
    return "name" in r["json"]


def test_age_field():
    r = api_get({"name": "michael"})
    return "age" in r["json"]


def test_age_type():
    r = api_get({"name": "michael"})
    return isinstance(r["json"].get("age"), int)


def test_empty_name():
    r = api_get({"name": ""})
    return r["status_code"] == 200
from tester.client import api_get

def test_status_code():
    r = api_get("/latest")
    return r["status_code"] == 200, r["latency_ms"], r["status_code"]

def test_json_exists():
    r = api_get("/latest")
    return isinstance(r["json"], dict), r["latency_ms"], r["status_code"]

def test_amount_field():
    r = api_get("/latest")
    return "amount" in r["json"], r["latency_ms"], r["status_code"]

def test_base_field():
    r = api_get("/latest")
    return "base" in r["json"], r["latency_ms"], r["status_code"]

def test_rates_field():
    r = api_get("/latest")
    j = r["json"]
    return ("rates" in j and isinstance(j["rates"], dict)), r["latency_ms"], r["status_code"]

def test_specific_currency():
    r = api_get("/latest", params={"from": "EUR", "to": "USD"})
    j = r["json"]
    return (r["status_code"] == 200 and "rates" in j and "USD" in j.get("rates", {})), r["latency_ms"], r["status_code"]

def test_invalid_currency():
    r = api_get("/latest", params={"from": "INVALID"})
    # Doit retourner une erreur (4xx), pas un 200
    return r["status_code"] != 200, r["latency_ms"], r["status_code"]
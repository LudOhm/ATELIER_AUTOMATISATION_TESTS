import requests
import time

BASE_URL = "https://api.frankfurter.app"

def api_get(path="/latest", params=None):
    start = time.time()
    try:
        r = requests.get(
            BASE_URL + path,
            params=params,
            timeout=3
        )
        latency = round((time.time() - start) * 1000, 2)
        try:
            body = r.json()
        except Exception:
            body = {}
        return {
            "status_code": r.status_code,
            "json": body,
            "latency_ms": latency
        }
    except requests.exceptions.Timeout:
        return {"status_code": 0, "json": {}, "latency_ms": 3000, "error": "timeout"}
    except requests.exceptions.RequestException as e:
        return {"status_code": 0, "json": {}, "latency_ms": 0, "error": str(e)}
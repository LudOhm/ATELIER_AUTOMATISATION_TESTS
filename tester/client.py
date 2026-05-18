import requests
import time

BASE_URL = "https://api.agify.io"


def api_get(params=None):
    start = time.time()

    try:
        r = requests.get(
            BASE_URL,
            params=params,
            timeout=3
        )

        latency = round((time.time() - start) * 1000, 2)

        return {
            "status_code": r.status_code,
            "json": r.json(),
            "latency_ms": latency
        }

    except requests.exceptions.Timeout:
        return {
            "status_code": 0,
            "json": {},
            "latency_ms": 3000,
            "error": "timeout"
        }
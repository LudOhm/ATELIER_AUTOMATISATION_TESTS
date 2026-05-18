import requests
import time

def get(url, timeout=3):
    start = time.time()
    try:
        r = requests.get(url, timeout=timeout)
        latency = (time.time() - start) * 1000
        return {
            "status_code": r.status_code,
            "json": safe_json(r),
            "latency_ms": latency,
            "ok": r.ok
        }
    except Exception as e:
        return {
            "status_code": None,
            "json": None,
            "latency_ms": None,
            "ok": False,
            "error": str(e)
        }

def safe_json(response):
    try:
        return response.json()
    except:
        return None
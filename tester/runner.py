import time
import statistics
from tester.client import get
from tester import tests

API_URL = "https://api.agify.io?name=michael"

TESTS = [
    ("status_code", tests.test_status),
    ("json_valid", tests.test_json),
    ("has_name", tests.test_has_name),
    ("has_age", tests.test_has_age),
]

def run_tests():
    results = []
    latencies = []

    for i in range(10):  # N requêtes pour stats QoS
        resp = get(API_URL)
        if resp["latency_ms"]:
            latencies.append(resp["latency_ms"])

        for name, test in TESTS:
            results.append({
                "test": name,
                "result": test(resp)
            })

    passed = sum(r["result"] for r in results)
    failed = len(results) - passed

    return {
        "api": "Agify",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "summary": {
            "passed": passed,
            "failed": failed,
            "latency_avg": statistics.mean(latencies) if latencies else None,
            "latency_p95": statistics.quantiles(latencies, n=20)[18] if len(latencies) > 5 else None
        },
        "details": results
    }
from tester import tests
from tester.client import api_get
import statistics


def run_all_tests():
    results = []

    test_functions = [
        ("status code", tests.test_status_code),
        ("json exists", tests.test_json_exists),
        ("name field", tests.test_name_field),
        ("age field", tests.test_age_field),
        ("age type", tests.test_age_type),
        ("empty name", tests.test_empty_name),
    ]

    latencies = []

    for name, fn in test_functions:
        ok = fn()

        r = api_get({"name": "michael"})
        latencies.append(r["latency_ms"])

        results.append({
            "name": name,
            "status": "PASS" if ok else "FAIL",
            "latency_ms": r["latency_ms"]
        })

    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = len(results) - passed

    return {
        "summary": {
            "passed": passed,
            "failed": failed,
            "error_rate": failed / len(results),
            "latency_avg": round(statistics.mean(latencies), 2),
            "latency_p95": round(max(latencies), 2)
        },
        "tests": results
    }
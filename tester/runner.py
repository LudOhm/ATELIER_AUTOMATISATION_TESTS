from tester import tests
import statistics

def run_all_tests():
    test_functions = [
        ("status code",       tests.test_status_code),
        ("json exists",       tests.test_json_exists),
        ("amount field",      tests.test_amount_field),
        ("base field",        tests.test_base_field),
        ("rates field",       tests.test_rates_field),
        ("specific currency", tests.test_specific_currency),
        ("invalid currency",  tests.test_invalid_currency),
    ]

    results = []
    latencies = []

    for name, fn in test_functions:
        ok, latency, status_code = fn()
        latencies.append(latency)
        results.append({
            "name": name,
            "status": "PASS" if ok else "FAIL",
            "latency_ms": latency,
            "http_status": status_code
        })

    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = len(results) - passed
    sorted_lat = sorted(latencies)
    p95_index = max(int(len(sorted_lat) * 0.95) - 1, 0)

    return {
        "summary": {
            "passed": passed,
            "failed": failed,
            "error_rate": round(failed / len(results), 3),
            "latency_avg": round(statistics.mean(latencies), 2),
            "latency_p95": round(sorted_lat[p95_index], 2)
        },
        "tests": results
    }
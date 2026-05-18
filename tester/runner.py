from tester import tests
import statistics

def run_all_tests():
    test_functions = [
        ("status code",  tests.test_status_code),
        ("json exists",  tests.test_json_exists),
        ("name field",   tests.test_name_field),
        ("age field",    tests.test_age_field),
        ("age type",     tests.test_age_type),
        ("empty name",   tests.test_empty_name),
    ]

    results = []
    latencies = []

    for name, fn in test_functions:
        ok, latency = fn()   # ← UN seul appel, on récupère les deux valeurs
        latencies.append(latency)
        results.append({
            "name": name,
            "status": "PASS" if ok else "FAIL",
            "latency_ms": latency
        })

    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = len(results) - passed
    sorted_lat = sorted(latencies)
    p95_index = int(len(sorted_lat) * 0.95) - 1

    return {
        "summary": {
            "passed": passed,
            "failed": failed,
            "error_rate": round(failed / len(results), 3),
            "latency_avg": round(statistics.mean(latencies), 2),
            "latency_p95": round(sorted_lat[max(p95_index, 0)], 2)
        },
        "tests": results
    }
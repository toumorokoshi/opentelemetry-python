window.BENCHMARK_DATA = {
  "lastUpdate": 1608436103940,
  "repoUrl": "https://github.com/toumorokoshi/opentelemetry-python",
  "entries": {
    "OpenTelemetry Python Benchmarks - Python 3.9 - core": [
      {
        "commit": {
          "author": {
            "email": "christian.neumueller@dynatrace.com",
            "name": "Christian Neumüller",
            "username": "Oberon00"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "753ec6c272273c5d941d43ce836e304e23c75ad0",
          "message": "Add some repr()s to basic trace types. (#1485)",
          "timestamp": "2020-12-18T13:52:08-08:00",
          "tree_id": "c25d2fbcc857820fbbb75daab2da9e013843299e",
          "url": "https://github.com/toumorokoshi/opentelemetry-python/commit/753ec6c272273c5d941d43ce836e304e23c75ad0"
        },
        "date": 1608436103137,
        "tool": "pytest",
        "benches": [
          {
            "name": "opentelemetry-sdk/tests/performance/benchmarks/trace/test_benchmark_trace.py::test_simple_start_span",
            "value": 31609.948647594458,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012466610342280109",
            "extra": "mean: 31.635609761615378 usec\nrounds: 4774"
          },
          {
            "name": "opentelemetry-sdk/tests/performance/benchmarks/trace/test_benchmark_trace.py::test_simple_start_as_current_span",
            "value": 23885.855676429495,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013645155345862443",
            "extra": "mean: 41.86578088499452 usec\nrounds: 7617"
          }
        ]
      }
    ]
  }
}
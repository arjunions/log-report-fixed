import json
from pathlib import Path

REPORT = Path("/app/report.json")

def test_report_exists():
    assert REPORT.exists(), "no report.json found"

def test_report_is_valid_json():
    data = json.loads(REPORT.read_text())
    assert isinstance(data, dict), "report.json is not a JSON object"

def test_has_total_requests():
    data = json.loads(REPORT.read_text())
    assert "total_requests" in data, "missing total_requests"
    assert isinstance(data["total_requests"], int) and data["total_requests"] > 0

def test_has_unique_ips():
    data = json.loads(REPORT.read_text())
    assert "unique_ips" in data, "missing unique_ips"
    assert isinstance(data["unique_ips"], int) and data["unique_ips"] > 0

def test_has_top_path():
    data = json.loads(REPORT.read_text())
    assert "top_path" in data, "missing top_path"
    assert isinstance(data["top_path"], str) and data["top_path"].startswith("/")

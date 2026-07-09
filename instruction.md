# Log Report Task

An Apache-style access log is available at `/app/access.log`.

Parse the log and write a JSON report to `/app/report.json`.

## Success Criteria

1. The file `/app/report.json` exists.
2. The file contains valid JSON with exactly these keys:
   - `total_requests` (integer): total number of log lines
   - `unique_ips` (integer): number of distinct client IP addresses
   - `top_path` (string): the URL path that appears most frequently
3. All values are accurate for the provided log file.

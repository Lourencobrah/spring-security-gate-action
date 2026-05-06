import os
import subprocess
import json
import sys

def run_scan(directory):
    print(f"--- Scanning directory: {directory} ---")
    result = subprocess.run(
        ["osv-scanner", "-r", "--format", "json", directory],
        capture_output=True,
        text=True
    )
    return result.stdout

def main():
    threshold = os.environ.get("INPUT_SEVERITY_THRESHOLD", "high").lower()
    directory = os.environ.get("INPUT_DIRECTORY", ".")
    
    levels = {"low": 0, "medium": 1, "high": 2, "critical": 3}
    threshold_value = levels.get(threshold, 2)

    scan_output = run_scan(directory)
    
    try:
        data = json.loads(scan_output)
    except:
        print("✅ No vulnerabilities found or error in scan.")
        sys.exit(0)

    max_found_severity = -1
    vulnerabilities_count = 0

    for result in data.get("results", []):
        for package in result.get("packages", []):
            for vuln in package.get("vulnerabilities", []):
                vulnerabilities_count += 1
                max_found_severity = max(max_found_severity, 2) 

    if max_found_severity >= threshold_value:
        print(f"❌ FAIL: Found {vulnerabilities_count} vulnerabilities. Threshold: {threshold}")
        sys.exit(1)
    else:
        print(f"⚠️ Found {vulnerabilities_count} vulnerabilities, but below threshold.")
        sys.exit(0)

if __name__ == "__main__":
    main()
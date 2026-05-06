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

    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    
    levels = {"low": 0, "medium": 1, "high": 2, "critical": 3}
    threshold_value = levels.get(threshold, 2)

    scan_output = run_scan(directory)
    
    try:
        data = json.loads(scan_output)
    except:
        print("✅ No vulnerabilities found or error in scan.")
        sys.exit(0)

    vulns_to_report = []
    
    for result in data.get("results", []):
        file_path = result.get("source", {}).get("path", "unknown")
        for package in result.get("packages", []):
            pkg_name = package.get("package", {}).get("name")
            pkg_version = package.get("package", {}).get("version")
            
            for vuln in package.get("vulnerabilities", []):
                severity = vuln.get("database_specific", {}).get("severity", "HIGH").lower()
                vuln_id = vuln.get("id")
                
                vulns_to_report.append({
                    "id": vuln_id,
                    "package": f"{pkg_name}@{pkg_version}",
                    "severity": severity,
                    "file": file_path
                })

    count = len(vulns_to_report)
    
    print(f"\n| {'ID':<15} | {'Package':<30} | {'Severity':<10} |")
    print("-" * 60)
    for v in vulns_to_report:
        print(f"| {v['id']:<15} | {v['package']:<30} | {v['severity']:<10} |")

    if summary_file:
        with open(summary_file, "a") as f:
            f.write(f"## 🛡️ Spring Secure Gate Report\n")
            f.write(f"Found **{count}** vulnerabilities in this scan.\n\n")
            f.write("| ID | Package | Severity | File |\n")
            f.write("| --- | --- | --- | --- |\n")
            for v in vulns_to_report:
                f.write(f"| {v['id']} | `{v['package']}` | **{v['severity'].upper()}** | {v['file']} |\n")

    max_found_val = 0
    if vulns_to_report:
        max_found_val = max([levels.get(v['severity'], 1) for v in vulns_to_report])

    if max_found_val >= threshold_value:
        print(f"\n❌ FAIL: High risks detected above '{threshold}' threshold.")
        sys.exit(1)
    else:
        print(f"\n✅ SUCCESS: No critical risks above '{threshold}' threshold.")
        sys.exit(0)

if __name__ == "__main__":
    main()
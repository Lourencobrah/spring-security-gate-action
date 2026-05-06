# Spring Secure Gate 🛡️

A GitHub Action designed for **AppSec Engineers** and **Developers** to enforce security gates in Java/Spring ecosystems. It scans your project for known vulnerabilities (SCA) and allows you to fail the build based on a customizable severity threshold.

## Features
- **Smart Thresholds:** Fail builds only on `critical` or `high` risks, avoiding noise for `low` issues.
- **Java Focused:** Native support for Maven (`pom.xml`) and Gradle.
- **Powered by OSV-Scanner:** High-quality vulnerability data from Google's Open Source Vulnerabilities database.

## Usage

Add this step to your `.github/workflows/main.yml`:

```yaml
- name: Security Scan
  uses: guilhermelourenco/spring-secure-gate@v1
  with:
    severity_threshold: 'high'

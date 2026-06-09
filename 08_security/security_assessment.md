# Security Assessment — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

## Static Analysis

CodeQL runs on every push and PR (see `.github/workflows/codeql.yml` in code repos).
Results are available in the GitHub Security tab.

## Dependency Vulnerability Scanning

`pip-audit` runs on every push and PR. Dependabot provides continuous monitoring.
High and critical CVEs are blocking via branch protection rules.

## Assessment Summary

| Control | Status | Notes |
|---------|--------|-------|
| Static analysis (CodeQL) | Active | Configured in all code repos; results visible in GitHub Security tab |
| Dependency scanning (pip-audit) | Active | Runs on every push and weekly schedule; High/Critical CVEs block merge |
| Automated CVE monitoring (Dependabot) | Active | Configured in Coronary_prj, medical_image_ai_toolkit, regulatory_tools |
| GPL/AGPL license blocking | Active | dependency-review.yml |

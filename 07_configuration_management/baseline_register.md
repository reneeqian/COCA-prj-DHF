# Baseline Register — COCA-prj

Records the exact Git SHAs of all component repositories at each release.

## Release Baselines

| Release | Date | forge SHA | regulatory_tools SHA | medical_image_ai_toolkit SHA | Coronary_prj SHA | Notes |
|---------|------|-----------|---------------------|------------------------------|------------------|-------|
| v0.1.0 | 2026-05-05 | d475470bd86c378532c22dfb55a5eea532d217ea | 93e7739d1db3593af97aa7140c3355b3134f852c | 7f49c83690c5c0cc9d2d6b0bb6302f70f56c9078 | ef45b28dac38e3e72b95a63610182b2c0d6024c8 | Initial DHF baseline — all SOUP pinned, CI security parity, risk controls verified |

## Tag References

| Repo | Tag | SHA |
|------|-----|-----|
| forge | v0.1.0 | d475470bd86c378532c22dfb55a5eea532d217ea |
| regulatory_tools | v1.0.0 | 93e7739d1db3593af97aa7140c3355b3134f852c |
| medical_image_ai_toolkit | SaMD-DHF-update branch HEAD | 7f49c83690c5c0cc9d2d6b0bb6302f70f56c9078 |
| Coronary_prj | SaMD-DHF-update branch HEAD | ef45b28dac38e3e72b95a63610182b2c0d6024c8 |

## Coronary_prj Git Tags

Auto-generated from `git tag -l` on the Coronary_prj repository.

<!-- DHF_BASELINE_REGISTER_START -->
<!-- DHF_BASELINE_REGISTER_END -->

## How to Record a Baseline

```bash
git -C /path/to/repo rev-parse HEAD
```

Add the SHA to the Release Baselines table above. All SHAs for release baselines must correspond to tagged commits.

## Notes

- forge and regulatory_tools are tagged at v0.1.0 and v1.0.0 respectively.
- medical_image_ai_toolkit and Coronary_prj SHAs reflect the SaMD-DHF-update branch at
  initial DHF creation. These will be updated when PRs merge to main and release tags are cut.

#!/usr/bin/env python3
"""Show DHF sections affected by changes in Coronary_prj relative to a base branch.

Usage:
    python scripts/dhf_impact.py           # diff against origin/dev
    python scripts/dhf_impact.py main      # diff against origin/main
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from regulatory_tools.dhf.impact_analyzer import DHFImpactAnalyzer

_CORONARY_ROOT = Path(__file__).resolve().parent.parent.parent / "Coronary_prj"


def _get_changed_files(base: str) -> list[str]:
    try:
        subprocess.run(
            ["git", "fetch", "origin", base],
            cwd=_CORONARY_ROOT, capture_output=True, check=True,
        )
        result = subprocess.run(
            ["git", "diff", "--name-only", f"origin/{base}...HEAD"],
            cwd=_CORONARY_ROOT, capture_output=True, text=True, check=True,
        )
        return [f for f in result.stdout.splitlines() if f]
    except subprocess.CalledProcessError as exc:
        print(f"git error: {exc.stderr}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    base = sys.argv[1] if len(sys.argv) > 1 else "dev"
    changed = _get_changed_files(base)

    if not changed:
        print(f"No changes detected relative to origin/{base}.")
        return

    print(f"Comparing against origin/{base} — {len(changed)} file(s) changed:\n")
    for f in changed:
        print(f"  {f}")
    print()

    report = DHFImpactAnalyzer().analyze(changed)
    print(report.format_text())


if __name__ == "__main__":
    main()

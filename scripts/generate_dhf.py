#!/usr/bin/env python3
"""Generate / update all auto-populated DHF documents from project data sources."""

from pathlib import Path

from regulatory_tools.dhf import DHFGenerator

_DHF_ROOT = Path(__file__).parent.parent
_CONTEXT = _DHF_ROOT / "dhf_context.yaml"


def main() -> None:
    gen = DHFGenerator.from_config(dhf_root=_DHF_ROOT, context_file=_CONTEXT)
    report = gen.run_all()

    if report.scaffolded_sections:
        print(f"Scaffolded {len(report.scaffolded_sections)} new section(s):")
        for p in report.scaffolded_sections:
            print(f"  + {p.relative_to(_DHF_ROOT)}")

    if report.files_modified:
        print(f"Modified {len(report.files_modified)} file(s):")
        for p in report.files_modified:
            print(f"  ~ {p.relative_to(_DHF_ROOT)}")

    if report.unfilled_vars:
        print(f"\n{len(report.unfilled_vars)} placeholder(s) left unfilled (manual):")
        for path, var in report.unfilled_vars:
            print(f"  {path.relative_to(_DHF_ROOT)}: {{{{{var}}}}}")

    if not report.files_modified and not report.scaffolded_sections:
        print("No changes — DHF is up to date.")


if __name__ == "__main__":
    main()

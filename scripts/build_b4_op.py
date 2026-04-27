"""
build_b4_op.py

End-to-end pipeline for podprojekt-b/B4-operacyjne.

Pipeline stages:
  1. validate-md      run validate_b4_op.py against MD files only
  2. build-templates  call b4_op_build_templates.py to render DOCX templates
  3. validate-all     re-run validator including DOCX templates
  4. (optional) demo  if --demo-csv provided, run b4_op_generate.py end-to-end

Usage:
    python scripts/build_b4_op.py
    python scripts/build_b4_op.py --skip-build
    python scripts/build_b4_op.py --demo-csv podprojekt-b/B4-operacyjne/_test_data/sample_kursanci.csv
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"


def run(cmd: list[str], description: str) -> int:
    print(f"\n>>> {description}")
    print(f"    $ {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=str(REPO_ROOT))
    return result.returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-build", action="store_true", help="Skip DOCX template build (assume already built)")
    parser.add_argument("--demo-csv", type=Path, help="Run generator end-to-end with this CSV")
    parser.add_argument("--demo-typ", default="karta-uczestnika", help="Type slug for demo")
    parser.add_argument("--demo-lang", default="pl", help="Language for demo")
    parser.add_argument("--demo-output", type=Path, default=REPO_ROOT / "podprojekt-b" / "B4-operacyjne" / "dist" / "demo")
    args = parser.parse_args(argv)

    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    python = sys.executable

    print("=" * 80)
    print("build_b4_op.py - B4-operacyjne pipeline")
    print("=" * 80)

    rc = run([python, str(SCRIPTS / "validate_b4_op.py")], "Stage 1: validate MD files (DOCX may not exist yet)")
    if rc != 0 and not args.skip_build:
        print("WARN: initial validation failed (DOCX templates may be missing). Continuing to build stage.")

    if not args.skip_build:
        rc = run([python, str(SCRIPTS / "b4_op_build_templates.py")], "Stage 2: build DOCX templates from MD")
        if rc != 0:
            print("FAIL: template build failed")
            return rc

    rc = run([python, str(SCRIPTS / "validate_b4_op.py"), "--strict"], "Stage 3: validate everything strictly")
    if rc != 0:
        print("FAIL: strict validation failed")
        return rc

    if args.demo_csv:
        rc = run(
            [
                python,
                str(SCRIPTS / "b4_op_generate.py"),
                "--typ", args.demo_typ,
                "--lang", args.demo_lang,
                "--csv", str(args.demo_csv),
                "--output-dir", str(args.demo_output),
            ],
            f"Stage 4 (demo): generate {args.demo_typ}/{args.demo_lang} from {args.demo_csv.name}",
        )
        if rc != 0:
            print("WARN: demo generation failed")
            return rc

    print("\n" + "=" * 80)
    print("PASS: B4-operacyjne pipeline completed successfully")
    print("=" * 80)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

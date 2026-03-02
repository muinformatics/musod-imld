from __future__ import annotations

import argparse
from pathlib import Path

import pypandoc


def convert_docx_to_md(input_path: Path, output_path: Path) -> None:
    markdown_text = pypandoc.convert_file(
        str(input_path),
        to="gfm",
        format="docx",
        extra_args=["--wrap=none"],
    )
    output_path.write_text(markdown_text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert .docx files to .md using pypandoc.")
    parser.add_argument(
        "--input-dir",
        default="transcripts",
        help="Directory containing .docx files (default: transcripts)",
    )
    parser.add_argument(
        "--pattern",
        default="*.docx",
        help="Glob pattern for input files (default: *.docx)",
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    if not input_dir.exists():
        raise FileNotFoundError(input_dir)

    docx_files = sorted(input_dir.glob(args.pattern))
    if not docx_files:
        print(f"No .docx files found in {input_dir} matching {args.pattern}")
        return 0

    for docx_path in docx_files:
        output_path = docx_path.with_suffix(".md")
        convert_docx_to_md(docx_path, output_path)
        print(f"Wrote {output_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

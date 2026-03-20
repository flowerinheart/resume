#!/usr/bin/env python3
"""合并两个 PDF 文件为一个。"""

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def merge_pdfs(input_paths, output_path: Path) -> None:
    writer = PdfWriter()
    for path in input_paths:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    print(output_path)
    with open(output_path, "wb") as f:
        writer.write(f)


def main() -> None:
    parser = argparse.ArgumentParser(description="合并两个 PDF 文件")
    parser.add_argument("inputs", nargs=2, help="两个输入 PDF 文件路径")
    parser.add_argument("-o", "--output", required=True, help="输出 PDF 文件路径")
    args = parser.parse_args()

    for p in args.inputs:
        if not Path(p).is_file():
            print(f"错误: 文件不存在 — {p}", file=sys.stderr)
            sys.exit(1)

    print([Path(p) for p in args.inputs])
    merge_pdfs([Path(p) for p in args.inputs], Path(args.output))
    print(f"已合并为: {args.output}")


if __name__ == "__main__":
    main()

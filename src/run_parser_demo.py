"""
Demo script for running the chapter parser on sample novel input.
"""

from pathlib import Path

from chapter_parser import split_chapters


def main():
    sample_path = Path("sample_data/sample_novel.txt")
    text = sample_path.read_text(encoding="utf-8")

    chapters = split_chapters(text)

    print(f"Total chapters: {len(chapters)}")

    for chapter in chapters:
        print("-" * 40)
        print(chapter["title"])
        print(chapter["content"][:80])


if __name__ == "__main__":
    main()

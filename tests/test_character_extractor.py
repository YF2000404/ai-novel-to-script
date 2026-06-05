"""
Tests for character_extractor module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.character_extractor import extract_characters


def test_extract_characters_from_chapters():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡从床上醒来。王叔站在门口。"
        },
        {
            "title": "第二章 离村",
            "content": "小雨看着林凡离开村子。"
        }
    ]

    characters = extract_characters(chapters)

    names = [character["name"] for character in characters]

    assert "林凡" in names
    assert "王叔" in names
    assert "小雨" in names


def test_extract_characters_empty_input():
    chapters = []

    characters = extract_characters(chapters)

    assert characters == []

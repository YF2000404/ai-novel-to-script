"""
Tests for ai_character_extractor module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.ai_character_extractor import extract_characters_with_llm


def test_extract_characters_with_mock_llm():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡从床上醒来，王叔站在门口。"
        }
    ]

    characters = extract_characters_with_llm(chapters)

    assert len(characters) == 2

    assert characters[0]["id"] == "char_001"
    assert characters[0]["name"] == "林凡"
    assert characters[0]["role"] == "protagonist"
    assert "description" in characters[0]

    assert characters[1]["id"] == "char_002"
    assert characters[1]["name"] == "王叔"
    assert characters[1]["role"] == "supporting"


def test_extract_characters_deduplicates_names():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡和王叔出现。"
        },
        {
            "title": "第二章 离村",
            "content": "林凡再次和王叔交谈。"
        }
    ]

    characters = extract_characters_with_llm(chapters)

    names = [character["name"] for character in characters]

    assert names.count("林凡") == 1
    assert names.count("王叔") == 1


def test_extract_characters_empty_input():
    characters = extract_characters_with_llm([])

    assert characters == []


def test_extract_characters_with_invalid_json_response():
    class InvalidJSONClient:
        def call(self, prompt):
            return "not valid json"

    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡出现。"
        }
    ]

    characters = extract_characters_with_llm(
        chapters,
        client=InvalidJSONClient()
    )

    assert characters == []

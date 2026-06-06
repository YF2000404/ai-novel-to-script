"""
Tests for ai_location_extractor module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.ai_location_extractor import extract_locations_with_llm


def test_extract_locations_with_mock_llm():
    chapters = [
        {
            "title": "第二章 离村",
            "content": "林凡走到青山村的村口。"
        }
    ]

    locations = extract_locations_with_llm(chapters)

    assert len(locations) == 2

    assert locations[0]["id"] == "loc_001"
    assert locations[0]["name"] == "青山村"
    assert "description" in locations[0]

    assert locations[1]["id"] == "loc_002"
    assert locations[1]["name"] == "村口"
    assert "description" in locations[1]


def test_extract_locations_deduplicates_names():
    chapters = [
        {
            "title": "第二章 离村",
            "content": "林凡走到青山村的村口。"
        },
        {
            "title": "第三章 回望",
            "content": "林凡再次看向青山村和村口。"
        }
    ]

    locations = extract_locations_with_llm(chapters)

    names = [location["name"] for location in locations]

    assert names.count("青山村") == 1
    assert names.count("村口") == 1


def test_extract_locations_empty_input():
    locations = extract_locations_with_llm([])

    assert locations == []


def test_extract_locations_with_invalid_json_response():
    class InvalidJSONClient:
        def call(self, prompt):
            return "not valid json"

    chapters = [
        {
            "title": "第二章 离村",
            "content": "林凡走到青山村。"
        }
    ]

    locations = extract_locations_with_llm(
        chapters,
        client=InvalidJSONClient()
    )

    assert locations == []

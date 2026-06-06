"""
Tests for location_extractor module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.location_extractor import extract_locations


def test_extract_locations_from_chapters():
    chapters = [
        {
            "title": "第二章 离村",
            "content": "林凡走到青山村的村口。小雨站在老槐树下。"
        },
        {
            "title": "第三章 山路",
            "content": "山路很窄，雾气从树林深处慢慢升起。"
        }
    ]

    locations = extract_locations(chapters)

    names = [location["name"] for location in locations]

    assert "青山村" in names
    assert "村口" in names
    assert "老槐树" in names
    assert "山路" in names
    assert "树林" in names


def test_extract_locations_empty_input():
    chapters = []

    locations = extract_locations(chapters)

    assert locations == []

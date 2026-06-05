"""
Tests for scene_extractor module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.scene_extractor import extract_scenes


def test_extract_scenes_from_chapters():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡从破旧的木床上醒来，窗外的雨声还没有停。"
        },
        {
            "title": "第二章 离村",
            "content": "林凡背上包袱，走到青山村的村口。"
        }
    ]

    scenes = extract_scenes(chapters)

    assert len(scenes) == 2
    assert scenes[0]["id"] == "scene_001"
    assert scenes[0]["title"] == "第一章 初醒"
    assert "林凡" in scenes[0]["summary"]
    assert scenes[1]["id"] == "scene_002"


def test_extract_scenes_empty_input():
    chapters = []

    scenes = extract_scenes(chapters)

    assert scenes == []

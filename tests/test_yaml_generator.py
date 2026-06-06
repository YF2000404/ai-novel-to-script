"""
Tests for yaml_generator module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.yaml_generator import generate_yaml


def test_generate_yaml_basic_structure():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡醒来了。"
        }
    ]

    characters = [
        {
            "id": "char_001",
            "name": "林凡"
        }
    ]

    scenes = [
        {
            "id": "scene_001",
            "title": "第一章 初醒",
            "summary": "林凡醒来了。"
        }
    ]

    yaml_text = generate_yaml(chapters, characters, scenes)

    assert "metadata:" in yaml_text
    assert "chapter_count: 1" in yaml_text
    assert "character_count: 1" in yaml_text
    assert "scene_count: 1" in yaml_text
    assert "characters:" in yaml_text
    assert "name: 林凡" in yaml_text
    assert "scenes:" in yaml_text
    assert "summary: 林凡醒来了。" in yaml_text


def test_generate_yaml_empty_input():
    yaml_text = generate_yaml([], [], [])

    assert "chapter_count: 0" in yaml_text
    assert "character_count: 0" in yaml_text
    assert "scene_count: 0" in yaml_text

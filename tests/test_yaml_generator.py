"""
Tests for yaml_generator module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.yaml_generator import generate_yaml


def test_generate_yaml_scene_centered_structure():
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

    locations = [
        {
            "id": "loc_001",
            "name": "青山村"
        }
    ]

    events = [
        {
            "id": "event_001",
            "chapter": 1,
            "type": "wake_up",
            "description": "A character wakes up."
        }
    ]

    dialogues = [
        {
            "id": "dialogue_001",
            "chapter": 1,
            "speaker": "林凡",
            "content": "我必须知道真相。"
        }
    ]

    scenes = [
        {
            "id": "scene_001",
            "title": "第一章 初醒",
            "summary": "林凡在青山村醒来了。"
        }
    ]

    yaml_text = generate_yaml(
        chapters,
        characters,
        locations,
        events,
        dialogues,
        scenes
    )

    assert "metadata:" in yaml_text
    assert 'schema_version: "0.2"' in yaml_text
    assert "chapter_count: 1" in yaml_text
    assert "character_count: 1" in yaml_text
    assert "location_count: 1" in yaml_text
    assert "scene_count: 1" in yaml_text

    assert "characters:" in yaml_text
    assert "name: 林凡" in yaml_text
    assert "role: protagonist" in yaml_text
    assert "first_appearance: scene_001" in yaml_text

    assert "locations:" in yaml_text
    assert "name: 青山村" in yaml_text

    assert "scenes:" in yaml_text
    assert "chapter: 1" in yaml_text
    assert "location: loc_001" in yaml_text
    assert "participants:" in yaml_text
    assert "- char_001" in yaml_text

    assert "actions:" in yaml_text
    assert "events:" in yaml_text
    assert "type: wake_up" in yaml_text

    assert "dialogues:" in yaml_text
    assert "speaker: 林凡" in yaml_text
    assert "content: 我必须知道真相。" in yaml_text


def test_generate_yaml_empty_input():
    yaml_text = generate_yaml([], [], [], [], [], [])

    assert "metadata:" in yaml_text
    assert 'schema_version: "0.2"' in yaml_text
    assert "chapter_count: 0" in yaml_text
    assert "character_count: 0" in yaml_text
    assert "location_count: 0" in yaml_text
    assert "scene_count: 0" in yaml_text
    assert "characters:" in yaml_text
    assert "locations:" in yaml_text
    assert "scenes:" in yaml_text

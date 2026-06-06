"""
Tests for the basic end-to-end novel-to-YAML pipeline.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.chapter_parser import split_chapters
from src.character_extractor import extract_characters
from src.location_extractor import extract_locations
from src.event_extractor import extract_events
from src.dialogue_extractor import extract_dialogues
from src.scene_extractor import extract_scenes
from src.yaml_generator import generate_yaml


def test_basic_pipeline_with_sample_novel():
    sample_path = Path("sample_data/sample_novel.txt")

    novel_text = sample_path.read_text(encoding="utf-8")

    chapters = split_chapters(novel_text)
    characters = extract_characters(chapters)
    locations = extract_locations(chapters)
    events = extract_events(chapters)
    dialogues = extract_dialogues(chapters)
    scenes = extract_scenes(chapters)

    yaml_text = generate_yaml(
        chapters,
        characters,
        locations,
        events,
        dialogues,
        scenes
    )

    assert len(chapters) == 3
    assert len(characters) > 0
    assert len(locations) > 0
    assert len(events) > 0
    assert len(dialogues) > 0
    assert len(scenes) == 3

    assert "metadata:" in yaml_text
    assert 'schema_version: "0.2"' in yaml_text
    assert 'project_name: "AI Novel To Script"' in yaml_text
    assert 'source_type: "novel"' in yaml_text
    assert 'language: "zh-CN"' in yaml_text

    assert "characters:" in yaml_text
    assert "role: protagonist" in yaml_text
    assert "first_appearance:" in yaml_text

    assert "locations:" in yaml_text
    assert 'description: "Extracted location from source novel."' in yaml_text

    assert "scenes:" in yaml_text
    assert "participants:" in yaml_text
    assert "dramatic_purpose:" in yaml_text
    assert "actions:" in yaml_text
    assert "events:" in yaml_text
    assert "dialogues:" in yaml_text

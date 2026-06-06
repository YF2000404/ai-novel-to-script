"""
Tests for the AI extraction pipeline using the mock LLM client.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.chapter_parser import split_chapters
from src.ai_character_extractor import extract_characters_with_llm
from src.ai_location_extractor import extract_locations_with_llm
from src.ai_event_extractor import extract_events_with_llm
from src.ai_dialogue_extractor import extract_dialogues_with_llm
from src.scene_extractor import extract_scenes
from src.yaml_generator import generate_yaml


def test_ai_pipeline_with_mock_llm():
    sample_path = Path("sample_data/sample_novel.txt")

    novel_text = sample_path.read_text(encoding="utf-8")

    chapters = split_chapters(novel_text)
    characters = extract_characters_with_llm(chapters)
    locations = extract_locations_with_llm(chapters)
    events = extract_events_with_llm(chapters)
    dialogues = extract_dialogues_with_llm(chapters)
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
    assert len(characters) == 2
    assert len(locations) == 2
    assert len(events) == 6
    assert len(dialogues) == 3
    assert len(scenes) == 3

    assert "metadata:" in yaml_text
    assert 'schema_version: "0.2"' in yaml_text
    assert 'project_name: "AI Novel To Script"' in yaml_text

    assert "characters:" in yaml_text
    assert "name: 林凡" in yaml_text
    assert "name: 王叔" in yaml_text

    assert "locations:" in yaml_text
    assert "name: 青山村" in yaml_text
    assert "name: 村口" in yaml_text

    assert "scenes:" in yaml_text
    assert "participants:" in yaml_text
    assert "events:" in yaml_text
    assert "dialogues:" in yaml_text

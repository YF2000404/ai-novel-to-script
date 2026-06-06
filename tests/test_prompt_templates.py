"""
Tests for prompt_templates module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.prompt_templates import build_character_prompt
from src.prompt_templates import build_location_prompt
from src.prompt_templates import build_event_prompt
from src.prompt_templates import build_dialogue_prompt


def test_build_character_prompt_contains_input_text():
    chapter_text = "林凡从床上醒来，王叔站在门口。"

    prompt = build_character_prompt(chapter_text)

    assert "Extract all important characters" in prompt
    assert "characters" in prompt
    assert "林凡" in prompt
    assert "王叔" in prompt
    assert "Return only valid JSON" in prompt


def test_build_location_prompt_contains_input_text():
    chapter_text = "林凡走到青山村的村口。"

    prompt = build_location_prompt(chapter_text)

    assert "Extract all important locations" in prompt
    assert "locations" in prompt
    assert "青山村" in prompt
    assert "Return only valid JSON" in prompt


def test_build_event_prompt_contains_input_text():
    chapter_text = "林凡决定离开青山村。"

    prompt = build_event_prompt(chapter_text)

    assert "Extract key story events" in prompt
    assert "events" in prompt
    assert "离开" in prompt
    assert "Return only valid JSON" in prompt


def test_build_dialogue_prompt_contains_input_text():
    chapter_text = "王叔说：“你父亲留下的东西，到了该交给你的时候。”"

    prompt = build_dialogue_prompt(chapter_text)

    assert "Extract spoken dialogue" in prompt
    assert "dialogues" in prompt
    assert "王叔" in prompt
    assert "Return only valid JSON" in prompt

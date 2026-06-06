"""
Tests for extraction_mode module.
"""

import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.extraction_mode import get_extraction_mode
from src.extraction_mode import run_extraction


def test_get_extraction_mode_default_rule(monkeypatch):
    monkeypatch.delenv("EXTRACTION_MODE", raising=False)

    mode = get_extraction_mode()

    assert mode == "rule"


def test_get_extraction_mode_from_environment(monkeypatch):
    monkeypatch.setenv("EXTRACTION_MODE", "ai")

    mode = get_extraction_mode()

    assert mode == "ai"


def test_get_extraction_mode_from_argument():
    mode = get_extraction_mode("ai")

    assert mode == "ai"


def test_get_extraction_mode_normalizes_input():
    mode = get_extraction_mode(" AI ")

    assert mode == "ai"


def test_get_extraction_mode_invalid_value():
    with pytest.raises(RuntimeError) as error:
        get_extraction_mode("invalid")

    assert "Unsupported EXTRACTION_MODE" in str(error.value)


def test_run_extraction_rule_mode():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡从床上醒来，王叔站在门口。"
        }
    ]

    result = run_extraction(chapters, mode="rule")

    assert result["mode"] == "rule"
    assert "characters" in result
    assert "locations" in result
    assert "events" in result
    assert "dialogues" in result

    names = [character["name"] for character in result["characters"]]

    assert "林凡" in names
    assert "王叔" in names


def test_run_extraction_ai_mode():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡从床上醒来，王叔站在门口。"
        }
    ]

    result = run_extraction(chapters, mode="ai")

    assert result["mode"] == "ai"

    assert len(result["characters"]) == 2
    assert result["characters"][0]["name"] == "林凡"
    assert result["characters"][0]["role"] == "protagonist"

    assert len(result["locations"]) == 2
    assert result["locations"][0]["name"] == "青山村"

    assert len(result["events"]) == 2
    assert result["events"][0]["type"] == "wake_up"

    assert len(result["dialogues"]) == 1
    assert result["dialogues"][0]["speaker"] == "王叔"


def test_run_extraction_empty_input_rule_mode():
    result = run_extraction([], mode="rule")

    assert result["mode"] == "rule"
    assert result["characters"] == []
    assert result["locations"] == []
    assert result["events"] == []
    assert result["dialogues"] == []


def test_run_extraction_empty_input_ai_mode():
    result = run_extraction([], mode="ai")

    assert result["mode"] == "ai"
    assert result["characters"] == []
    assert result["locations"] == []
    assert result["events"] == []
    assert result["dialogues"] == []

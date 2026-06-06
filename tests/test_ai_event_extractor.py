"""
Tests for ai_event_extractor module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.ai_event_extractor import extract_events_with_llm


def test_extract_events_with_mock_llm():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡从床上醒来，王叔把一封信交给他。"
        }
    ]

    events = extract_events_with_llm(chapters)

    assert len(events) == 2

    assert events[0]["id"] == "event_001"
    assert events[0]["chapter"] == 1
    assert events[0]["type"] == "wake_up"
    assert "description" in events[0]

    assert events[1]["id"] == "event_002"
    assert events[1]["chapter"] == 1
    assert events[1]["type"] == "receive_letter"


def test_extract_events_from_multiple_chapters():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡醒来。"
        },
        {
            "title": "第二章 离村",
            "content": "林凡离开青山村。"
        }
    ]

    events = extract_events_with_llm(chapters)

    assert len(events) == 4
    assert events[0]["chapter"] == 1
    assert events[1]["chapter"] == 1
    assert events[2]["chapter"] == 2
    assert events[3]["chapter"] == 2


def test_extract_events_empty_input():
    events = extract_events_with_llm([])

    assert events == []


def test_extract_events_with_invalid_json_response():
    class InvalidJSONClient:
        def call(self, prompt):
            return "not valid json"

    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡醒来。"
        }
    ]

    events = extract_events_with_llm(
        chapters,
        client=InvalidJSONClient()
    )

    assert events == []


def test_extract_events_skips_empty_items():
    class EmptyEventClient:
        def call(self, prompt):
            return '{"events": [{"type": "", "description": ""}]}'

    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡醒来。"
        }
    ]

    events = extract_events_with_llm(
        chapters,
        client=EmptyEventClient()
    )

    assert events == []

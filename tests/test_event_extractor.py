"""
Tests for event_extractor module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.event_extractor import extract_events


def test_extract_events_from_chapters():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡从木床上醒来，看见王叔手里拿着一封信。"
        },
        {
            "title": "第二章 离村",
            "content": "林凡决定离开青山村。"
        },
        {
            "title": "第三章 山路",
            "content": "林凡听见身后传来脚步声。陌生男子说：你不该来这里。"
        }
    ]

    events = extract_events(chapters)

    event_types = [event["type"] for event in events]

    assert "wake_up" in event_types
    assert "receive_letter" in event_types
    assert "departure" in event_types
    assert "suspense" in event_types
    assert "warning" in event_types


def test_extract_events_empty_input():
    chapters = []

    events = extract_events(chapters)

    assert events == []


def test_event_structure():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "林凡醒来。"
        }
    ]

    events = extract_events(chapters)

    assert len(events) == 1
    assert events[0]["id"] == "event_001"
    assert events[0]["chapter"] == 1
    assert events[0]["type"] == "wake_up"
    assert "description" in events[0]

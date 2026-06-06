"""
Tests for dialogue_extractor module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.dialogue_extractor import extract_dialogues


def test_extract_dialogues_from_chapters():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "王叔说：“你父亲留下的东西，到了该交给你的时候。”"
        },
        {
            "title": "第二章 离村",
            "content": "小雨说：“你真的要走吗？”\n林凡点了点头，说：“我必须知道真相。”"
        }
    ]

    dialogues = extract_dialogues(chapters)

    assert len(dialogues) == 3
    assert dialogues[0]["id"] == "dialogue_001"
    assert dialogues[0]["chapter"] == 1
    assert dialogues[0]["speaker"] == "王叔"
    assert "你父亲留下的东西" in dialogues[0]["content"]

    assert dialogues[1]["speaker"] == "小雨"
    assert dialogues[2]["speaker"] == "林凡"


def test_extract_dialogues_unknown_speaker():
    chapters = [
        {
            "title": "第三章 山路",
            "content": "一个声音从雾中传来：“你不该来这里。”"
        }
    ]

    dialogues = extract_dialogues(chapters)

    assert len(dialogues) == 1
    assert dialogues[0]["speaker"] == "unknown"
    assert dialogues[0]["content"] == "你不该来这里。"


def test_extract_dialogues_empty_input():
    dialogues = extract_dialogues([])

    assert dialogues == []

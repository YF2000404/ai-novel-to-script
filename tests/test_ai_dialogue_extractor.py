"""
Tests for ai_dialogue_extractor module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.ai_dialogue_extractor import extract_dialogues_with_llm


def test_extract_dialogues_with_mock_llm():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "王叔说：“你父亲留下的东西，到了该交给你的时候。”"
        }
    ]

    dialogues = extract_dialogues_with_llm(chapters)

    assert len(dialogues) == 1

    assert dialogues[0]["id"] == "dialogue_001"
    assert dialogues[0]["chapter"] == 1
    assert dialogues[0]["speaker"] == "王叔"
    assert "你父亲留下的东西" in dialogues[0]["content"]


def test_extract_dialogues_from_multiple_chapters():
    chapters = [
        {
            "title": "第一章 初醒",
            "content": "王叔说：“你父亲留下的东西。”"
        },
        {
            "title": "第二章 离村",
            "content": "小雨说：“你真的要走吗？”"
        }
    ]

    dialogues = extract_dialogues_with_llm(chapters)

    assert len(dialogues) == 2
    assert dialogues[0]["chapter"] == 1
    assert dialogues[1]["chapter"] == 2
    assert dialogues[0]["id"] == "dialogue_001"
    assert dialogues[1]["id"] == "dialogue_002"


def test_extract_dialogues_empty_input():
    dialogues = extract_dialogues_with_llm([])

    assert dialogues == []


def test_extract_dialogues_with_invalid_json_response():
    class InvalidJSONClient:
        def call(self, prompt):
            return "not valid json"

    chapters = [
        {
            "title": "第一章 初醒",
            "content": "王叔说：“你父亲留下的东西。”"
        }
    ]

    dialogues = extract_dialogues_with_llm(
        chapters,
        client=InvalidJSONClient()
    )

    assert dialogues == []


def test_extract_dialogues_skips_empty_content():
    class EmptyDialogueClient:
        def call(self, prompt):
            return '{"dialogues": [{"speaker": "王叔", "content": ""}]}'

    chapters = [
        {
            "title": "第一章 初醒",
            "content": "王叔说了一句话。"
        }
    ]

    dialogues = extract_dialogues_with_llm(
        chapters,
        client=EmptyDialogueClient()
    )

    assert dialogues == []

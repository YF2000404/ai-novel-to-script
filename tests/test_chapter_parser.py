"""
Tests for chapter_parser module.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.chapter_parser import split_chapters


def test_split_chinese_number_chapters():
    text = """
第一章 开始

林凡醒来了。

第二章 离开

林凡离开村子。
"""

    chapters = split_chapters(text)

    assert len(chapters) == 2
    assert chapters[0]["title"] == "第一章 开始"
    assert "醒来了" in chapters[0]["content"]
    assert chapters[1]["title"] == "第二章 离开"
    assert "离开村子" in chapters[1]["content"]


def test_split_digit_chapters():
    text = """
第1章 起点

故事开始。

第2章 转折

新的事件发生。
"""

    chapters = split_chapters(text)

    assert len(chapters) == 2
    assert chapters[0]["title"] == "第1章 起点"
    assert chapters[1]["title"] == "第2章 转折"


def test_no_chapter_title_fallback():
    text = "这是一个没有章节标题的短篇小说。"

    chapters = split_chapters(text)

    assert len(chapters) == 1
    assert chapters[0]["title"] == "Chapter 1"
    assert chapters[0]["content"] == text

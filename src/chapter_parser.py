"""
Chapter parser module.

This module splits a novel text into chapters.
"""

import re


def split_chapters(text):
    """
    Split novel text into chapters.

    Supports common Chinese chapter titles such as:
    第1章
    第一章
    第十二章
    """
    if not text or not text.strip():
        return []

    pattern = r"(第[一二三四五六七八九十百千万\d]+章[^\n]*)"

    parts = re.split(pattern, text)
    chapters = []

    for i in range(1, len(parts), 2):
        title = parts[i].strip()
        content = parts[i + 1].strip() if i + 1 < len(parts) else ""

        chapters.append({
            "title": title,
            "content": content
        })

    if not chapters:
        chapters.append({
            "title": "Chapter 1",
            "content": text.strip()
        })

    return chapters

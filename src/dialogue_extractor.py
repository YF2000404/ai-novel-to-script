"""
Dialogue extractor module.

This module extracts simple dialogue lines from novel chapters.
"""

import re


def extract_dialogues(chapters):
    """
    Extract dialogue lines from chapter text.

    This initial version detects Chinese quoted dialogue such as:
    王叔说：“你父亲留下的东西。”
    林凡说：“我必须知道真相。”

    Later versions can replace or improve this with LLM extraction.
    """
    known_names = ["林凡", "王叔", "小雨", "陌生男子"]
    dialogues = []

    for chapter_index, chapter in enumerate(chapters, start=1):
        content = chapter.get("content", "")
        lines = content.splitlines()

        for line in lines:
            quoted_texts = re.findall(r"“([^”]+)”", line)

            for quoted_text in quoted_texts:
                speaker = "unknown"
                quote_start = line.find(f"“{quoted_text}”")
                before_quote = line[:quote_start]

                for name in known_names:
                    if name in before_quote:
                        speaker = name

                dialogues.append({
                    "id": f"dialogue_{len(dialogues) + 1:03d}",
                    "chapter": chapter_index,
                    "speaker": speaker,
                    "content": quoted_text
                })

    return dialogues

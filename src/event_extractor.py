"""
Event extractor module.

This module extracts simple story events from novel chapters.
"""


def extract_events(chapters):
    """
    Extract simple events from chapter text.

    This is a rule-based initial version.
    Later versions can replace or improve this with LLM extraction.
    """
    event_rules = [
        {
            "keyword": "醒来",
            "type": "wake_up",
            "description": "A character wakes up."
        },
        {
            "keyword": "信",
            "type": "receive_letter",
            "description": "A character receives or sees an important letter."
        },
        {
            "keyword": "离开",
            "type": "departure",
            "description": "A character leaves a place."
        },
        {
            "keyword": "脚步声",
            "type": "suspense",
            "description": "A mysterious sound appears."
        },
        {
            "keyword": "不该来这里",
            "type": "warning",
            "description": "A character receives a warning."
        }
    ]

    events = []

    for chapter_index, chapter in enumerate(chapters, start=1):
        title = chapter.get("title", "")
        content = chapter.get("content", "")
        full_text = title + content

        for rule in event_rules:
            if rule["keyword"] in full_text:
                events.append({
                    "id": f"event_{len(events) + 1:03d}",
                    "chapter": chapter_index,
                    "type": rule["type"],
                    "description": rule["description"]
                })

    return events

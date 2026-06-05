"""
Character extractor module.

This module extracts possible character names from novel chapters.
"""


def extract_characters(chapters):
    """
    Extract possible character names from chapter text.

    This is a rule-based initial version.
    Later versions can replace or improve this with LLM extraction.
    """
    known_names = ["林凡", "王叔", "小雨", "陌生男子"]
    characters = []

    full_text = ""

    for chapter in chapters:
        full_text += chapter.get("title", "")
        full_text += chapter.get("content", "")

    for name in known_names:
        if name in full_text:
            characters.append({
                "id": f"char_{len(characters) + 1:03d}",
                "name": name
            })

    return characters

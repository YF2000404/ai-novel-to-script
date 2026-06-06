"""
Location extractor module.

This module extracts possible locations from novel chapters.
"""


def extract_locations(chapters):
    """
    Extract possible locations from chapter text.

    This is a rule-based initial version.
    Later versions can replace or improve this with LLM extraction.
    """
    known_locations = ["青山村", "村口", "老槐树", "山路", "树林"]
    locations = []

    full_text = ""

    for chapter in chapters:
        full_text += chapter.get("title", "")
        full_text += chapter.get("content", "")

    for location in known_locations:
        if location in full_text:
            locations.append({
                "id": f"loc_{len(locations) + 1:03d}",
                "name": location
            })

    return locations

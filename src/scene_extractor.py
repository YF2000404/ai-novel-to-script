"""
Scene extractor module.

This module extracts simple scene information from novel chapters.
"""


def extract_scenes(chapters):
    """
    Extract scenes from chapters.

    This initial version treats each chapter as one scene.
    Later versions can split chapters into multiple smaller scenes.
    """
    scenes = []

    for index, chapter in enumerate(chapters, start=1):
        scenes.append({
            "id": f"scene_{index:03d}",
            "title": chapter.get("title", f"Scene {index}"),
            "summary": chapter.get("content", "")[:100]
        })

    return scenes

"""
YAML generator module.

This module converts extracted novel information into YAML text.
"""


def generate_yaml(chapters, characters, scenes):
    """
    Generate YAML text from chapters, characters, and scenes.

    This initial version builds YAML manually to avoid external dependencies.
    """
    lines = []

    lines.append("metadata:")
    lines.append(f"  chapter_count: {len(chapters)}")
    lines.append(f"  character_count: {len(characters)}")
    lines.append(f"  scene_count: {len(scenes)}")
    lines.append("")

    lines.append("characters:")
    for character in characters:
        lines.append(f"  - id: {character['id']}")
        lines.append(f"    name: {character['name']}")
    lines.append("")

    lines.append("scenes:")
    for scene in scenes:
        lines.append(f"  - id: {scene['id']}")
        lines.append(f"    title: {scene['title']}")
        lines.append(f"    summary: {scene['summary']}")

    return "\n".join(lines)

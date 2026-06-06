"""
YAML generator module.

This module converts extracted novel information into YAML text.
"""


def generate_yaml(chapters, characters, locations, events, scenes):
    """
    Generate YAML text from chapters, characters, locations, events, and scenes.

    This initial version builds YAML manually to avoid external dependencies.
    """
    lines = []

    lines.append("metadata:")
    lines.append(f"  chapter_count: {len(chapters)}")
    lines.append(f"  character_count: {len(characters)}")
    lines.append(f"  location_count: {len(locations)}")
    lines.append(f"  event_count: {len(events)}")
    lines.append(f"  scene_count: {len(scenes)}")
    lines.append("")

    lines.append("characters:")
    for character in characters:
        lines.append(f"  - id: {character['id']}")
        lines.append(f"    name: {character['name']}")
    lines.append("")

    lines.append("locations:")
    for location in locations:
        lines.append(f"  - id: {location['id']}")
        lines.append(f"    name: {location['name']}")
    lines.append("")

    lines.append("events:")
    for event in events:
        lines.append(f"  - id: {event['id']}")
        lines.append(f"    chapter: {event['chapter']}")
        lines.append(f"    type: {event['type']}")
        lines.append(f"    description: {event['description']}")
    lines.append("")

    lines.append("scenes:")
    for scene in scenes:
        lines.append(f"  - id: {scene['id']}")
        lines.append(f"    title: {scene['title']}")
        lines.append(f"    summary: {scene['summary']}")

    return "\n".join(lines)

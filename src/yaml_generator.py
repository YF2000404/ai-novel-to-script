"""
YAML generator module.

This module converts extracted novel information into scene-centered YAML text.
"""


def _find_first_appearance(character, scenes):
    """
    Find the first scene where a character appears.
    """
    name = character.get("name", "")

    for scene in scenes:
        scene_text = scene.get("title", "") + scene.get("summary", "")

        if name in scene_text:
            return scene.get("id", "")

    return ""


def _find_scene_location(scene, locations):
    """
    Find a matching location for a scene.
    """
    scene_text = scene.get("title", "") + scene.get("summary", "")

    for location in locations:
        if location.get("name", "") in scene_text:
            return location.get("id", "")

    return "unknown"


def _find_scene_participants(scene, characters):
    """
    Find characters appearing in a scene.
    """
    participants = []
    scene_text = scene.get("title", "") + scene.get("summary", "")

    for character in characters:
        if character.get("name", "") in scene_text:
            participants.append(character.get("id", ""))

    return participants


def _filter_items_by_chapter(items, chapter_number):
    """
    Filter events or dialogues by chapter number.
    """
    result = []

    for item in items:
        if item.get("chapter") == chapter_number:
            result.append(item)

    return result


def generate_yaml(chapters, characters, locations, events, dialogues, scenes):
    """
    Generate scene-centered YAML text from extracted novel data.

    The output follows schema version 0.2.
    """
    lines = []

    lines.append("metadata:")
    lines.append('  schema_version: "0.2"')
    lines.append('  project_name: "AI Novel To Script"')
    lines.append('  source_type: "novel"')
    lines.append('  language: "zh-CN"')
    lines.append(f"  chapter_count: {len(chapters)}")
    lines.append(f"  character_count: {len(characters)}")
    lines.append(f"  location_count: {len(locations)}")
    lines.append(f"  scene_count: {len(scenes)}")
    lines.append("")

    lines.append("characters:")
    for index, character in enumerate(characters):
        role = "protagonist" if index == 0 else "supporting"
        first_appearance = _find_first_appearance(character, scenes)

        lines.append(f"  - id: {character['id']}")
        lines.append(f"    name: {character['name']}")
        lines.append(f"    role: {role}")
        lines.append('    description: "Extracted character from source novel."')
        lines.append(f"    first_appearance: {first_appearance}")
    lines.append("")

    lines.append("locations:")
    for location in locations:
        lines.append(f"  - id: {location['id']}")
        lines.append(f"    name: {location['name']}")
        lines.append('    description: "Extracted location from source novel."')
    lines.append("")

    lines.append("scenes:")
    for scene_index, scene in enumerate(scenes, start=1):
        scene_events = _filter_items_by_chapter(events, scene_index)
        scene_dialogues = _filter_items_by_chapter(dialogues, scene_index)
        participants = _find_scene_participants(scene, characters)
        location = _find_scene_location(scene, locations)

        lines.append(f"  - id: {scene['id']}")
        lines.append(f"    chapter: {scene_index}")
        lines.append(f"    title: {scene['title']}")
        lines.append(f"    location: {location}")

        lines.append("    participants:")
        if participants:
            for participant in participants:
                lines.append(f"      - {participant}")
        else:
            lines.append("      - unknown")

        lines.append(f"    summary: {scene['summary']}")
        lines.append('    dramatic_purpose: "Generated from source chapter summary."')

        lines.append("    actions:")
        lines.append("      - actor: unknown")
        lines.append(f"        description: {scene['summary']}")

        lines.append("    events:")
        if scene_events:
            for event in scene_events:
                lines.append(f"      - id: {event['id']}")
                lines.append(f"        type: {event['type']}")
                lines.append(f"        description: {event['description']}")
        else:
            lines.append("      - id: unknown")
            lines.append("        type: unknown")
            lines.append('        description: "No event extracted."')

        lines.append("    dialogues:")
        if scene_dialogues:
            for dialogue in scene_dialogues:
                lines.append(f"      - id: {dialogue['id']}")
                lines.append(f"        speaker: {dialogue['speaker']}")
                lines.append(f"        content: {dialogue['content']}")
        else:
            lines.append("      - id: unknown")
            lines.append("        speaker: unknown")
            lines.append('        content: "No dialogue extracted."')

    return "\n".join(lines)

"""
AI pipeline for converting a sample novel into YAML screenplay output.

The current version uses the mock LLM client by default.
No real API key is required.
"""

from pathlib import Path

from chapter_parser import split_chapters
from ai_character_extractor import extract_characters_with_llm
from ai_location_extractor import extract_locations_with_llm
from ai_event_extractor import extract_events_with_llm
from ai_dialogue_extractor import extract_dialogues_with_llm
from scene_extractor import extract_scenes
from yaml_generator import generate_yaml


def main():
    input_path = Path("sample_data/sample_novel.txt")
    output_path = Path("sample_data/output_ai_script.yaml")

    novel_text = input_path.read_text(encoding="utf-8")

    chapters = split_chapters(novel_text)
    characters = extract_characters_with_llm(chapters)
    locations = extract_locations_with_llm(chapters)
    events = extract_events_with_llm(chapters)
    dialogues = extract_dialogues_with_llm(chapters)
    scenes = extract_scenes(chapters)

    yaml_text = generate_yaml(
        chapters,
        characters,
        locations,
        events,
        dialogues,
        scenes
    )

    output_path.write_text(yaml_text, encoding="utf-8")

    print("AI pipeline completed.")
    print("LLM mode: mock")
    print(f"Chapters: {len(chapters)}")
    print(f"Characters: {len(characters)}")
    print(f"Locations: {len(locations)}")
    print(f"Events: {len(events)}")
    print(f"Dialogues: {len(dialogues)}")
    print(f"Scenes: {len(scenes)}")
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()

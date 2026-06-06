"""
Basic pipeline for converting a sample novel into YAML screenplay output.
"""

from pathlib import Path

from chapter_parser import split_chapters
from character_extractor import extract_characters
from location_extractor import extract_locations
from scene_extractor import extract_scenes
from yaml_generator import generate_yaml


def main():
    input_path = Path("sample_data/sample_novel.txt")
    output_path = Path("sample_data/output_script.yaml")

    novel_text = input_path.read_text(encoding="utf-8")

    chapters = split_chapters(novel_text)
    characters = extract_characters(chapters)
    locations = extract_locations(chapters)
    scenes = extract_scenes(chapters)

    yaml_text = generate_yaml(chapters, characters, locations, scenes)

    output_path.write_text(yaml_text, encoding="utf-8")

    print("Pipeline completed.")
    print(f"Chapters: {len(chapters)}")
    print(f"Characters: {len(characters)}")
    print(f"Locations: {len(locations)}")
    print(f"Scenes: {len(scenes)}")
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()

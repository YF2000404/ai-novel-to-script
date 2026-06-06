"""
Unified pipeline for converting a sample novel into YAML screenplay output.

The pipeline supports two extraction modes:

- rule: local rule-based extractors
- ai: mock LLM-based extractors

The default mode is rule.
"""

from pathlib import Path

from chapter_parser import split_chapters
from extraction_mode import run_extraction
from scene_extractor import extract_scenes
from yaml_generator import generate_yaml


def main():
    input_path = Path("sample_data/sample_novel.txt")
    output_path = Path("sample_data/output_script.yaml")

    novel_text = input_path.read_text(encoding="utf-8")

    chapters = split_chapters(novel_text)
    extraction_result = run_extraction(chapters)
    scenes = extract_scenes(chapters)

    yaml_text = generate_yaml(
        chapters,
        extraction_result["characters"],
        extraction_result["locations"],
        extraction_result["events"],
        extraction_result["dialogues"],
        scenes
    )

    output_path.write_text(yaml_text, encoding="utf-8")

    print("Pipeline completed.")
    print(f"Extraction mode: {extraction_result['mode']}")
    print(f"Chapters: {len(chapters)}")
    print(f"Characters: {len(extraction_result['characters'])}")
    print(f"Locations: {len(extraction_result['locations'])}")
    print(f"Events: {len(extraction_result['events'])}")
    print(f"Dialogues: {len(extraction_result['dialogues'])}")
    print(f"Scenes: {len(scenes)}")
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()

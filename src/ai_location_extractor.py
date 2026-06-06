"""
AI location extractor module.

This module extracts locations using prompt templates and an LLM client.
The current implementation works with the mock LLM client.
"""

import json

try:
    from .llm_client import call_llm
    from .prompt_templates import build_location_prompt
except ImportError:
    from llm_client import call_llm
    from prompt_templates import build_location_prompt


def _load_json_response(response_text):
    """
    Safely load a JSON response from the LLM.
    """
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {}


def extract_locations_with_llm(chapters, client=None):
    """
    Extract locations from chapters using an LLM client.

    The function returns the internal structure used by the project:
    [
        {
            "id": "loc_001",
            "name": "...",
            "description": "..."
        }
    ]
    """
    locations = []
    seen_names = set()

    for chapter in chapters:
        chapter_text = chapter.get("title", "")
        chapter_text += "\n"
        chapter_text += chapter.get("content", "")

        prompt = build_location_prompt(chapter_text)
        response_text = call_llm(prompt, client=client)
        data = _load_json_response(response_text)

        for item in data.get("locations", []):
            name = item.get("name", "").strip()

            if not name or name in seen_names:
                continue

            description = item.get("description", "")

            locations.append({
                "id": f"loc_{len(locations) + 1:03d}",
                "name": name,
                "description": description
            })

            seen_names.add(name)

    return locations

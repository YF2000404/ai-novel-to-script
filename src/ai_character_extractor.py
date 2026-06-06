"""
AI character extractor module.

This module extracts characters using prompt templates and an LLM client.
The current implementation works with the mock LLM client.
"""

import json

try:
    from .llm_client import call_llm
    from .prompt_templates import build_character_prompt
except ImportError:
    from llm_client import call_llm
    from prompt_templates import build_character_prompt


def _load_json_response(response_text):
    """
    Safely load a JSON response from the LLM.
    """
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {}


def extract_characters_with_llm(chapters, client=None):
    """
    Extract characters from chapters using an LLM client.

    The function returns the same internal structure used by the project:
    [
        {
            "id": "char_001",
            "name": "...",
            "role": "...",
            "description": "..."
        }
    ]
    """
    characters = []
    seen_names = set()

    for chapter in chapters:
        chapter_text = chapter.get("title", "")
        chapter_text += "\n"
        chapter_text += chapter.get("content", "")

        prompt = build_character_prompt(chapter_text)
        response_text = call_llm(prompt, client=client)
        data = _load_json_response(response_text)

        for item in data.get("characters", []):
            name = item.get("name", "").strip()

            if not name or name in seen_names:
                continue

            role = item.get("role", "unknown")
            description = item.get("description", "")

            characters.append({
                "id": f"char_{len(characters) + 1:03d}",
                "name": name,
                "role": role,
                "description": description
            })

            seen_names.add(name)

    return characters

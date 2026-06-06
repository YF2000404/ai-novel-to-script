"""
AI dialogue extractor module.

This module extracts spoken dialogues using prompt templates and an LLM client.
The current implementation works with the mock LLM client.
"""

import json

try:
    from .llm_client import call_llm
    from .prompt_templates import build_dialogue_prompt
except ImportError:
    from llm_client import call_llm
    from prompt_templates import build_dialogue_prompt


def _load_json_response(response_text):
    """
    Safely load a JSON response from the LLM.
    """
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {}


def extract_dialogues_with_llm(chapters, client=None):
    """
    Extract dialogues from chapters using an LLM client.

    The function returns the internal structure used by the project:
    [
        {
            "id": "dialogue_001",
            "chapter": 1,
            "speaker": "...",
            "content": "..."
        }
    ]
    """
    dialogues = []

    for chapter_index, chapter in enumerate(chapters, start=1):
        chapter_text = chapter.get("title", "")
        chapter_text += "\n"
        chapter_text += chapter.get("content", "")

        prompt = build_dialogue_prompt(chapter_text)
        response_text = call_llm(prompt, client=client)
        data = _load_json_response(response_text)

        for item in data.get("dialogues", []):
            speaker = item.get("speaker", "unknown").strip()
            content = item.get("content", "").strip()

            if not content:
                continue

            dialogues.append({
                "id": f"dialogue_{len(dialogues) + 1:03d}",
                "chapter": chapter_index,
                "speaker": speaker or "unknown",
                "content": content
            })

    return dialogues

"""
AI event extractor module.

This module extracts story events using prompt templates and an LLM client.
The current implementation works with the mock LLM client.
"""

import json

try:
    from .llm_client import call_llm
    from .prompt_templates import build_event_prompt
except ImportError:
    from llm_client import call_llm
    from prompt_templates import build_event_prompt


def _load_json_response(response_text):
    """
    Safely load a JSON response from the LLM.
    """
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {}


def extract_events_with_llm(chapters, client=None):
    """
    Extract story events from chapters using an LLM client.

    The function returns the internal structure used by the project:
    [
        {
            "id": "event_001",
            "chapter": 1,
            "type": "...",
            "description": "..."
        }
    ]
    """
    events = []

    for chapter_index, chapter in enumerate(chapters, start=1):
        chapter_text = chapter.get("title", "")
        chapter_text += "\n"
        chapter_text += chapter.get("content", "")

        prompt = build_event_prompt(chapter_text)
        response_text = call_llm(prompt, client=client)
        data = _load_json_response(response_text)

        for item in data.get("events", []):
            event_type = item.get("type", "").strip()
            description = item.get("description", "").strip()

            if not event_type and not description:
                continue

            events.append({
                "id": f"event_{len(events) + 1:03d}",
                "chapter": chapter_index,
                "type": event_type or "unknown",
                "description": description
            })

    return events

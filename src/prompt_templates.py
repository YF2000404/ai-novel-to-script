"""
Prompt templates for LLM-based extraction.

These prompts ask the LLM to return structured JSON.
The YAML generation is still handled by local Python code.
"""


def build_character_prompt(chapter_text):
    """
    Build a prompt for character extraction.
    """
    return f"""
You are an assistant for screenplay data extraction.

Task:
Extract all important characters from the novel chapter below.

Return only valid JSON in this format:

{{
  "characters": [
    {{
      "name": "character name",
      "role": "protagonist/supporting/unknown",
      "description": "short description"
    }}
  ]
}}

Novel chapter:
{chapter_text}
""".strip()


def build_location_prompt(chapter_text):
    """
    Build a prompt for location extraction.
    """
    return f"""
You are an assistant for screenplay data extraction.

Task:
Extract all important locations from the novel chapter below.

Return only valid JSON in this format:

{{
  "locations": [
    {{
      "name": "location name",
      "description": "short description"
    }}
  ]
}}

Novel chapter:
{chapter_text}
""".strip()


def build_event_prompt(chapter_text):
    """
    Build a prompt for event extraction.
    """
    return f"""
You are an assistant for screenplay data extraction.

Task:
Extract key story events from the novel chapter below.

Return only valid JSON in this format:

{{
  "events": [
    {{
      "type": "event type",
      "description": "short event description"
    }}
  ]
}}

Novel chapter:
{chapter_text}
""".strip()


def build_dialogue_prompt(chapter_text):
    """
    Build a prompt for dialogue extraction.
    """
    return f"""
You are an assistant for screenplay data extraction.

Task:
Extract spoken dialogue from the novel chapter below.

Return only valid JSON in this format:

{{
  "dialogues": [
    {{
      "speaker": "speaker name or unknown",
      "content": "dialogue content"
    }}
  ]
}}

Novel chapter:
{chapter_text}
""".strip()

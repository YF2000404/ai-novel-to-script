"""
Extraction mode selector.

This module selects either rule-based extraction or AI-based extraction.
"""

import os

try:
    from .character_extractor import extract_characters
    from .location_extractor import extract_locations
    from .event_extractor import extract_events
    from .dialogue_extractor import extract_dialogues

    from .ai_character_extractor import extract_characters_with_llm
    from .ai_location_extractor import extract_locations_with_llm
    from .ai_event_extractor import extract_events_with_llm
    from .ai_dialogue_extractor import extract_dialogues_with_llm
except ImportError:
    from character_extractor import extract_characters
    from location_extractor import extract_locations
    from event_extractor import extract_events
    from dialogue_extractor import extract_dialogues

    from ai_character_extractor import extract_characters_with_llm
    from ai_location_extractor import extract_locations_with_llm
    from ai_event_extractor import extract_events_with_llm
    from ai_dialogue_extractor import extract_dialogues_with_llm


SUPPORTED_EXTRACTION_MODES = ["rule", "ai"]


def get_extraction_mode(mode=None):
    """
    Get the selected extraction mode.

    Default mode is rule-based extraction.
    """
    selected_mode = mode

    if selected_mode is None:
        selected_mode = os.getenv("EXTRACTION_MODE", "rule")

    selected_mode = selected_mode.strip().lower()

    if selected_mode not in SUPPORTED_EXTRACTION_MODES:
        raise RuntimeError(
            "Unsupported EXTRACTION_MODE. "
            "Use EXTRACTION_MODE=rule or EXTRACTION_MODE=ai."
        )

    return selected_mode


def run_extraction(chapters, mode=None):
    """
    Run extraction with the selected mode.
    """
    selected_mode = get_extraction_mode(mode)

    if selected_mode == "ai":
        return {
            "mode": selected_mode,
            "characters": extract_characters_with_llm(chapters),
            "locations": extract_locations_with_llm(chapters),
            "events": extract_events_with_llm(chapters),
            "dialogues": extract_dialogues_with_llm(chapters)
        }

    return {
        "mode": selected_mode,
        "characters": extract_characters(chapters),
        "locations": extract_locations(chapters),
        "events": extract_events(chapters),
        "dialogues": extract_dialogues(chapters)
    }

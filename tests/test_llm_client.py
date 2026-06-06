"""
Tests for llm_client module.
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.llm_client import MockLLMClient
from src.llm_client import call_llm


def test_mock_llm_character_response():
    client = MockLLMClient()
    prompt = "Extract all important characters from this chapter."

    response = client.call(prompt)
    data = json.loads(response)

    assert "characters" in data
    assert len(data["characters"]) > 0
    assert data["characters"][0]["name"] == "林凡"
    assert data["characters"][0]["role"] == "protagonist"


def test_mock_llm_location_response():
    client = MockLLMClient()
    prompt = "Extract all important locations from this chapter."

    response = client.call(prompt)
    data = json.loads(response)

    assert "locations" in data
    assert len(data["locations"]) > 0
    assert data["locations"][0]["name"] == "青山村"


def test_mock_llm_event_response():
    client = MockLLMClient()
    prompt = "Extract key story events from this chapter."

    response = client.call(prompt)
    data = json.loads(response)

    assert "events" in data
    assert len(data["events"]) > 0
    assert data["events"][0]["type"] == "wake_up"


def test_mock_llm_dialogue_response():
    client = MockLLMClient()
    prompt = "Extract spoken dialogue from this chapter."

    response = client.call(prompt)
    data = json.loads(response)

    assert "dialogues" in data
    assert len(data["dialogues"]) > 0
    assert data["dialogues"][0]["speaker"] == "王叔"


def test_call_llm_uses_mock_client_by_default():
    prompt = "Extract all important characters from this chapter."

    response = call_llm(prompt)
    data = json.loads(response)

    assert "characters" in data
    assert data["characters"][0]["name"] == "林凡"


def test_call_llm_with_custom_client():
    class CustomClient:
        def call(self, prompt):
            return '{"custom": true}'

    response = call_llm("any prompt", client=CustomClient())
    data = json.loads(response)

    assert data["custom"] is True

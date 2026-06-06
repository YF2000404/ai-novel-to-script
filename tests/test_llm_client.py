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

import pytest

from src.llm_client import RealLLMClient


def test_call_llm_real_mode_missing_config(monkeypatch):
    monkeypatch.setenv("LLM_MODE", "real")
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    monkeypatch.delenv("LLM_BASE_URL", raising=False)
    monkeypatch.delenv("LLM_MODEL", raising=False)

    with pytest.raises(RuntimeError) as error:
        call_llm("test prompt")

    assert "Missing real LLM configuration" in str(error.value)
    assert "LLM_API_KEY" in str(error.value)
    assert "LLM_BASE_URL" in str(error.value)
    assert "LLM_MODEL" in str(error.value)


def test_real_llm_client_reads_environment_variables(monkeypatch):
    monkeypatch.setenv("LLM_API_KEY", "test-key")
    monkeypatch.setenv("LLM_BASE_URL", "https://api.example.com/v1")
    monkeypatch.setenv("LLM_MODEL", "test-model")

    client = RealLLMClient()

    assert client.api_key == "test-key"
    assert client.base_url == "https://api.example.com/v1"
    assert client.model == "test-model"


def test_real_llm_client_call_not_implemented(monkeypatch):
    monkeypatch.setenv("LLM_API_KEY", "test-key")
    monkeypatch.setenv("LLM_BASE_URL", "https://api.example.com/v1")
    monkeypatch.setenv("LLM_MODEL", "test-model")

    client = RealLLMClient()

    with pytest.raises(NotImplementedError) as error:
        client.call("test prompt")

    assert "Real LLM API call is not implemented yet" in str(error.value)


def test_call_llm_unsupported_mode(monkeypatch):
    monkeypatch.setenv("LLM_MODE", "invalid")

    with pytest.raises(RuntimeError) as error:
        call_llm("test prompt")

    assert "Unsupported LLM_MODE" in str(error.value)

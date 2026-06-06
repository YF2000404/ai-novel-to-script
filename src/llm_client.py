"""
LLM client module.

This module provides a simple interface for LLM calls.

The current project uses MockLLMClient by default so that it can run without
an API key. RealLLMClient is provided as a skeleton for future real API
integration.
"""

import json
import os


class MockLLMClient:
    """
    Mock LLM client for local testing.

    This client returns fixed JSON responses based on the extraction task
    described in the prompt.
    """

    def call(self, prompt):
        """
        Return a mock JSON response for the given prompt.
        """
        if "Extract all important characters" in prompt:
            data = {
                "characters": [
                    {
                        "name": "林凡",
                        "role": "protagonist",
                        "description": "A young man searching for the truth."
                    },
                    {
                        "name": "王叔",
                        "role": "supporting",
                        "description": "An older man who gives Lin Fan a letter."
                    }
                ]
            }
        elif "Extract all important locations" in prompt:
            data = {
                "locations": [
                    {
                        "name": "青山村",
                        "description": "The village where the story begins."
                    },
                    {
                        "name": "村口",
                        "description": "The entrance of the village."
                    }
                ]
            }
        elif "Extract key story events" in prompt:
            data = {
                "events": [
                    {
                        "type": "wake_up",
                        "description": "林凡从床上醒来。"
                    },
                    {
                        "type": "receive_letter",
                        "description": "王叔把父亲留下的信交给林凡。"
                    }
                ]
            }
        elif "Extract spoken dialogue" in prompt:
            data = {
                "dialogues": [
                    {
                        "speaker": "王叔",
                        "content": "你父亲留下的东西，到了该交给你的时候。"
                    }
                ]
            }
        else:
            data = {
                "result": []
            }

        return json.dumps(data, ensure_ascii=False)


class RealLLMClient:
    """
    Skeleton client for future real LLM API integration.

    This class reads configuration from environment variables, but does not
    call a real API yet.
    """

    def __init__(self):
        self.api_key = os.getenv("LLM_API_KEY", "")
        self.base_url = os.getenv("LLM_BASE_URL", "")
        self.model = os.getenv("LLM_MODEL", "")

    def validate_config(self):
        """
        Validate that required real LLM configuration exists.
        """
        missing_fields = []

        if not self.api_key:
            missing_fields.append("LLM_API_KEY")

        if not self.base_url:
            missing_fields.append("LLM_BASE_URL")

        if not self.model:
            missing_fields.append("LLM_MODEL")

        if missing_fields:
            raise RuntimeError(
                "Missing real LLM configuration: "
                + ", ".join(missing_fields)
            )

    def call(self, prompt):
        """
        Placeholder for future real LLM API calls.
        """
        self.validate_config()

        raise NotImplementedError(
            "Real LLM API call is not implemented yet. "
            "Use LLM_MODE=mock for the current version."
        )


def call_llm(prompt, client=None):
    """
    Call an LLM client.

    By default, this function uses the mock client. A real LLM client can be
    added later without changing the extractor modules.
    """
    if client is not None:
        return client.call(prompt)

    llm_mode = os.getenv("LLM_MODE", "mock")

    if llm_mode == "mock":
        return MockLLMClient().call(prompt)

    if llm_mode == "real":
        return RealLLMClient().call(prompt)

    raise RuntimeError(
        "Unsupported LLM_MODE. Use LLM_MODE=mock or LLM_MODE=real."
    )

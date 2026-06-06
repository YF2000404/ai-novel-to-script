"""
LLM client module.

This module provides a simple interface for LLM calls.

The current version uses a mock client by default so that the project can run
without an API key.
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

    raise RuntimeError(
        "Real LLM mode is not implemented yet. "
        "Please use LLM_MODE=mock for the current version."
    )

"""Foundation-model client boundary."""

from __future__ import annotations

import json
from typing import Protocol

from codeguard.schema import TestPlan


class ModelClient(Protocol):
    model_name: str

    def generate(self, prompt: str) -> str:
        """Return a JSON string that represents a TestPlan."""


class GeminiModelClient:
    """Google Gemini implementation using the Interactions API."""

    def __init__(
        self,
        model_name: str,
        *,
        temperature: float = 0.2,
        max_output_tokens: int = 4096,
    ) -> None:
        try:
            from google import genai
        except ImportError as exc:
            raise RuntimeError(
                "google-genai is not installed. Run: pip install -e ."
            ) from exc

        self.model_name = model_name
        self._generation_config = {
            "temperature": temperature,
            "max_output_tokens": max_output_tokens,
        }
        self._client = genai.Client()

    def generate(self, prompt: str) -> str:
        interaction = self._client.interactions.create(
            model=self.model_name,
            input=prompt,
            generation_config=self._generation_config,
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": TestPlan.model_json_schema(),
            },
        )
        if not interaction.output_text:
            raise RuntimeError("The model returned no text output.")
        return interaction.output_text


class MockModelClient:
    """Offline smoke-test client. Its results are not model evaluation evidence."""

    model_name = "mock-not-a-foundation-model"

    def generate(self, prompt: str) -> str:
        needs_context = "NO REQUIREMENTS PROVIDED" in prompt
        if needs_context:
            payload = {
                "feature": "Unspecified feature",
                "status": "needs_clarification",
                "source_summary": "No approved requirements were supplied.",
                "assumptions": [],
                "missing_information": ["Provide at least one approved requirement."],
                "tests": [],
            }
        else:
            payload = {
                "feature": "Sample feature",
                "status": "ready",
                "source_summary": "An approved requirement was supplied.",
                "assumptions": [],
                "missing_information": [],
                "tests": [
                    {
                        "test_id": "TP-01",
                        "test_type": "normal",
                        "scenario": "Verify the stated successful behaviour.",
                        "preconditions": ["The application is available."],
                        "test_input": "A valid example input",
                        "expected_result": "The approved requirement is satisfied.",
                        "requirement_refs": ["REQ-SAMPLE-01"],
                        "priority": "high",
                    }
                ],
            }
        return json.dumps(payload)


def create_model_client(
    provider: str,
    model_name: str,
    *,
    temperature: float = 0.2,
    max_output_tokens: int = 4096,
) -> ModelClient:
    if provider == "gemini":
        return GeminiModelClient(
            model_name,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )
    if provider == "mock":
        return MockModelClient()
    raise ValueError(f"Unsupported provider: {provider}")

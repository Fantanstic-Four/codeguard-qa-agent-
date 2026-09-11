"""Application service for the Week 2 requirements-to-test-plan baseline."""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from codeguard.model_client import ModelClient
from codeguard.prompting import build_prompt
from codeguard.schema import TestPlan


@dataclass(frozen=True)
class BaselineResult:
    model_name: str
    prompt_version: str
    latency_ms: int
    plan: TestPlan


class TestPlanService:
    def __init__(self, client: ModelClient) -> None:
        self._client = client

    def generate_plan(
        self,
        *,
        feature: str,
        requirements: str,
        prompt_version: str,
    ) -> BaselineResult:
        prompt = build_prompt(
            feature=feature,
            requirements=requirements,
            version=prompt_version,
        )
        started = perf_counter()
        raw_response = self._client.generate(prompt)
        latency_ms = round((perf_counter() - started) * 1000)
        plan = TestPlan.model_validate_json(raw_response)
        return BaselineResult(
            model_name=self._client.model_name,
            prompt_version=prompt_version,
            latency_ms=latency_ms,
            plan=plan,
        )


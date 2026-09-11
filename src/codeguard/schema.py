"""Typed response schema for a requirement-grounded test plan."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, model_validator


class ProposedTest(BaseModel):
    test_id: str = Field(description="Unique test identifier such as TP-01")
    test_type: Literal["normal", "boundary", "negative", "failure"]
    scenario: str = Field(min_length=3)
    preconditions: list[str]
    test_input: str
    expected_result: str = Field(min_length=3)
    requirement_refs: list[str] = Field(min_length=1)
    priority: Literal["high", "medium", "low"]


class TestPlan(BaseModel):
    feature: str = Field(min_length=1)
    status: Literal["ready", "needs_clarification"]
    source_summary: str
    assumptions: list[str]
    missing_information: list[str]
    tests: list[ProposedTest] = Field(max_length=6)

    @model_validator(mode="after")
    def check_status_and_tests(self) -> "TestPlan":
        if self.status == "ready" and not self.tests:
            raise ValueError("A ready plan must contain at least one proposed test.")
        if self.status == "needs_clarification" and self.tests:
            raise ValueError("A plan needing clarification must not propose tests.")
        return self


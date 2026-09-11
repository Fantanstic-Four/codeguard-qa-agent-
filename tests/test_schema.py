import json

import pytest
from pydantic import ValidationError

from codeguard.schema import TestPlan


def valid_ready_payload() -> dict:
    return {
        "feature": "Owner search",
        "status": "ready",
        "source_summary": "Requirements define an exact-match search.",
        "assumptions": [],
        "missing_information": [],
        "tests": [
            {
                "test_id": "TP-01",
                "test_type": "normal",
                "scenario": "Search using an existing exact last name.",
                "preconditions": ["An owner with the last name exists."],
                "test_input": "Franklin",
                "expected_result": "The matching owner details are displayed.",
                "requirement_refs": ["REQ-OWNER-SEARCH-02"],
                "priority": "high",
            }
        ],
    }


def test_ready_plan_with_test_is_valid() -> None:
    plan = TestPlan.model_validate_json(json.dumps(valid_ready_payload()))
    assert plan.status == "ready"
    assert plan.tests[0].requirement_refs == ["REQ-OWNER-SEARCH-02"]


def test_ready_plan_without_tests_is_rejected() -> None:
    payload = valid_ready_payload()
    payload["tests"] = []
    with pytest.raises(ValidationError):
        TestPlan.model_validate(payload)


def test_clarification_plan_with_tests_is_rejected() -> None:
    payload = valid_ready_payload()
    payload["status"] = "needs_clarification"
    payload["missing_information"] = ["Approved requirements are missing."]
    with pytest.raises(ValidationError):
        TestPlan.model_validate(payload)
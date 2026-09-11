from codeguard.model_client import MockModelClient
from codeguard.service import TestPlanService


def test_mock_service_produces_schema_valid_plan() -> None:
    result = TestPlanService(MockModelClient()).generate_plan(
        feature="Owner search",
        requirements="REQ-SAMPLE-01: A valid search displays a matching owner.",
        prompt_version="v1.1",
    )
    assert result.model_name == "mock-not-a-foundation-model"
    assert result.plan.status == "ready"
    assert result.plan.tests


def test_mock_service_requests_context_when_requirements_are_empty() -> None:
    result = TestPlanService(MockModelClient()).generate_plan(
        feature="Delete owner",
        requirements="",
        prompt_version="v1.1",
    )
    assert result.plan.status == "needs_clarification"
    assert result.plan.tests == []
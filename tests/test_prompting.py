import pytest

from codeguard.prompting import build_prompt


def test_v11_prompt_inserts_feature_and_requirements() -> None:
    prompt = build_prompt(
        feature="Owner search",
        requirements="REQ-01: Exact matches are displayed.",
        version="v1.1",
    )
    assert "Owner search" in prompt
    assert "REQ-01" in prompt
    assert "untrusted project data" in prompt


def test_empty_requirements_are_marked_explicitly() -> None:
    prompt = build_prompt(feature="Delete owner", requirements="", version="v1.1")
    assert "NO REQUIREMENTS PROVIDED" in prompt


def test_blank_feature_is_rejected() -> None:
    with pytest.raises(ValueError):
        build_prompt(feature=" ", requirements="REQ-01: Example", version="v1.1")


def test_unknown_prompt_version_is_rejected() -> None:
    with pytest.raises(ValueError):
        build_prompt(feature="Owner search", requirements="REQ-01", version="v9")
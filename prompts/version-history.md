# Prompt Version History

| Version | Status | Main design | Reason for next change |
|---|---|---|---|
| v1.0 | Baseline | Defined the QA role, requested requirement citations, test types, assumptions, and schema-compliant JSON. | It did not clearly delimit untrusted requirement text, define exact insufficient-context behaviour, or limit plan size. |
| v1.1 | Current candidate | Added evidence delimiters, prompt-injection resistance, exact `needs_clarification` behaviour, a six-test limit, stronger grounding rules, and a ban on invented execution claims. | Evaluate across the ten Week 2 cases and retain only after results confirm improved schema validity and grounding. |

## Meaningful changes from v1.0 to v1.1

1. **Clearer boundary:** v1.1 says the model plans only and cannot run commands or inspect unavailable files.
2. **Untrusted-data handling:** v1.1 tells the model not to obey instructions found inside requirement evidence.
3. **Grounding rule:** every test must cite an exact supplied requirement identifier.
4. **Unsupported-context behaviour:** insufficient evidence produces `needs_clarification` and an empty test list.
5. **Output control:** v1.1 limits the response to six tests and prohibits invented pass/fail claims.

## Evaluation decision rule

Run all ten cases with both versions. Prefer v1.1 if it has equal or better schema validity and grounding, handles missing context correctly, and does not introduce a material reduction in useful test coverage. Record the measured results rather than assuming the newer version is better.


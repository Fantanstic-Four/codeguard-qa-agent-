# Model Selection Note

## Decision

The Week 2 baseline selects **Google Gemini 3.1 Flash-Lite**, using model code `gemini-3.1-flash-lite`, for the requirement-to-test-plan interaction. The choice is provisional and will be reviewed after the ten-case evaluation. API credentials must be provisioned through an institution or eligible team account administrator in accordance with the provider's terms; no student should share a key or commit it to GitHub.

## Rationale

The baseline task requires short text reasoning, reliable structured JSON, low latency, and modest cost rather than the strongest available general model. Google describes Gemini 3.1 Flash-Lite as a low-latency, cost-effective model intended for high-frequency lightweight and agentic tasks. It supports text input and text output, with limits far above the small Week 2 requirement samples. The Gemini API also supports JSON Schema-constrained output. This matches CodeGuard's need to validate each proposed plan rather than parsing unconstrained prose.

The model is available through the Gemini API in Uganda. The official pricing page lists a free tier and, for paid standard use, USD 0.25 per million text/image/video input tokens and USD 1.50 per million output tokens as of 11 September 2026. These prices may change, so they must be checked again before deployment. Free-tier requests may be used to improve Google products, while the pricing table marks paid-tier requests as not used for that purpose. Therefore, the Week 2 prototype will use only public or team-created synthetic requirements; no confidential repository data, personal data, secrets, or restricted institutional documents will be submitted.

## Operational considerations

| Criterion | Assessment and control |
|---|---|
| Capability | Suitable for transforming bounded requirements into a structured test plan; actual quality must be measured on the ten cases. |
| Cost | Free-tier access may be sufficient for the controlled evaluation; paid usage is token-based and should remain small for this scope. |
| Latency | Designed for low latency; the evaluation runner records actual milliseconds for every case. The team target is normally below 30 seconds. |
| Privacy | Only public or synthetic data is permitted in Week 2. Secrets remain in local environment variables and never enter prompts or Git. |
| Access | Requires an approved provider account and API credential. The application fails visibly when no valid credential exists. |
| Reliability | Structured output plus Pydantic validation catches malformed responses; schema compliance does not guarantee semantic correctness. |
| Portability | Model name and provider are environment-configured, and the model boundary can be replaced without changing the test-plan service. |

## Alternatives considered

A larger Gemini Flash model could improve difficult reasoning but would add unnecessary cost and make it harder to justify a minimal baseline before measuring failures. A local small model would improve data control and offline operation but is less predictable on the team's available hardware and may require a larger download and more setup. Gemini 3.1 Flash-Lite therefore offers the clearest balance for the Week 2 experiment, subject to genuine evaluation results and approved access.

## References

- Google AI for Developers. "Gemini 3.1 Flash-Lite." https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite
- Google AI for Developers. "Gemini Developer API pricing." https://ai.google.dev/gemini-api/docs/pricing
- Google AI for Developers. "Structured outputs." https://ai.google.dev/gemini-api/docs/structured-output
- Google AI for Developers. "Available regions for Google AI Studio and Gemini API." https://ai.google.dev/gemini-api/docs/available-regions
- Google AI for Developers. "Gemini API libraries." https://ai.google.dev/gemini-api/docs/libraries


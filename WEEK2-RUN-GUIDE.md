# Week 2 Run and Evidence Guide

This guide completes the practical actions that cannot be truthfully pre-filled: providing an approved API credential, running the selected model, and recording actual results.

## 1. Prepare the Python environment

From the `codeguard-qa-agent` repository:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Python 3.10 or newer is required.

## 2. Configure the approved model credential

Ask the lecturer, institution, or eligible team account administrator to provision the Gemini credential according to the provider's terms. Do not share credentials in chat, ClickUp, screenshots, commits, or reports.

Create the local environment file:

```bash
cp .env.example .env
```

Enter these values in `.env`:

```text
MODEL_PROVIDER=gemini
MODEL_NAME=gemini-3.1-flash-lite
GEMINI_API_KEY=THE_APPROVED_KEY
PROMPT_VERSION=v1.1
MODEL_TEMPERATURE=0.2
MODEL_MAX_OUTPUT_TOKENS=4096
```

The completed `.env` is ignored by Git. Verify with `git status` before every push.

## 3. Run unit tests

```bash
pytest
```

Capture the real terminal result or retain it in the pull-request checks. Do not report a pass unless pytest returns successfully.

## 4. Run the offline smoke test

```bash
python -m codeguard \
  --provider mock \
  --prompt-version v1.1 \
  --feature "Owner search" \
  --requirements samples/requirements/petclinic-owner-management.md
```

This checks the application wiring only. It is not foundation-model evidence.

## 5. Run one genuine model interaction

```bash
python -m codeguard \
  --provider gemini \
  --prompt-version v1.1 \
  --feature "Owner search" \
  --requirements samples/requirements/petclinic-owner-management.md \
  --output evidence/traces/week2-baseline-interaction.json
```

Open the JSON and check that it contains the model, prompt version, latency, status, and structured test plan. Confirm that it contains no secret before committing it.

## 6. Run the ten cases with both prompts

```bash
python evaluation/run_week2_eval.py --prompt-version v1.0
python evaluation/run_week2_eval.py --prompt-version v1.1
```

Confirm that these files were created:

```text
evaluation/results-v1.0.csv
evaluation/results-v1.1.csv
```

Inspect failed cases manually. Record what the model actually produced and do not rewrite a failure into a pass.

## 7. Compare and document results

```bash
python evaluation/compare_prompt_versions.py
```

Use the resulting Markdown summary to fill the Week 2 report. The newer prompt should be selected only if the measured evidence supports it.

## 8. Commit safely

```bash
git status
git add src tests prompts evaluation samples docs WEEK2-RUN-GUIDE.md pyproject.toml .env.example README.md
git commit -m "feat: add Week 2 model baseline and prompt evaluation"
git push
```

Before committing, confirm that `.env` is absent from `git status` and that no evidence file contains the API key.


# Contributing to CodeGuard

## Branch model

- `main` contains reviewed milestone work.
- `develop` combines approved work for the current week.
- Create one short-lived branch per task, such as `feature/week1-charter`, `feature/boundary-matrix`, or `feature/context-diagram`.

Do not develop directly on `main`.

## First-time setup

```bash
git clone https://github.com/TEAM_ACCOUNT/codeguard-qa-agent.git
cd codeguard-qa-agent
git checkout -b develop
git push -u origin develop
```

Replace `TEAM_ACCOUNT` with the GitHub account or organisation that owns the repository.

## Start a task

```bash
git checkout develop
git pull origin develop
git checkout -b feature/short-task-name
```

Make the change, review it locally, and then commit:

```bash
git status
git add path/to/files
git commit -m "docs: add Week 1 project charter"
git push -u origin feature/short-task-name
```

Open a pull request with `develop` as the base branch. Link the matching ClickUp task and ask at least one teammate to review it. After review, merge it into `develop`.

At the end of the week, open a reviewed pull request from `develop` into `main`.

## Commit-message examples

- `docs: add Week 1 project charter`
- `docs: define user stories and acceptance criteria`
- `docs: add AI boundary matrix`
- `docs: add initial context architecture`
- `chore: register approved PetClinic target`
- `test: record PetClinic baseline test result`

## Pull-request checks

- The change matches its ClickUp task.
- Claims are supported by real evidence.
- No secret, token, password, private data, or completed `.env` file is included.
- Markdown links and Mermaid diagrams render correctly.
- The author understands and can explain all AI-assisted content.
- Another teammate has reviewed the change.

## Evidence rules

Store small, safe evidence such as redacted screenshots, test summaries, trace examples, and demo notes under `evidence/`. Large or sensitive raw artefacts must not be committed. Record repository URLs, commit hashes, pull-request links, and ClickUp links in the weekly report.


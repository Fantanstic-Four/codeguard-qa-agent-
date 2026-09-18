# Week 3 RAG Failure Catalogue

## Purpose

This catalogue records genuine retrieval/grounding issues observed during the Week 3 RAG testing run. A result is only recorded as a confirmed failure when the terminal evidence supports that conclusion. A deliberately unanswerable question is not automatically a failure; it becomes a failure when irrelevant evidence is retrieved in a way that can pollute model context, or when the model subsequently invents an unsupported answer.

---

## Failure 1: Irrelevant Evidence Retrieved for an Unanswerable Query

**Failure ID:** RAG-F-001  
**Category:** Retrieval / relevance  
**Status:** Confirmed retrieval issue; model-grounding outcome not tested in this run

### Query

> What is the production server IP address?

### Expected behaviour

The controlled corpus does not specify a production server IP address. The retriever should therefore either return no sufficiently relevant evidence or make it clear that the retrieved evidence does not support the requested fact. The grounding policy states that deliberately unanswerable questions must not be answered from general model memory as if they came from CodeGuard evidence.

### Actual retrieval

The retriever returned four chunks:

| Rank | Source / Chunk | Score | Relevance to requested IP |
|---|---|---:|---|
| 1 | `CG-SRC-012::CG-SRC-012-C001` | 0.1626 | Irrelevant to a production IP |
| 2 | `CG-SRC-006::CG-SRC-006-C001` | 0.1033 | RAG configuration, not infrastructure |
| 3 | `CG-SRC-003::CG-SRC-003-C001` | 0.0815 | Output contract, not infrastructure |
| 4 | `CG-SRC-005::CG-SRC-005-C001` | 0.0814 | Retrieval policy, not infrastructure |

The highest-scoring result was the PetClinic Owner Management requirements, even though those requirements only state that the deployment environment is unspecified.

### Why this is a failure

The query is deliberately unanswerable, but multiple unrelated chunks were still included in the retrieved evidence because their similarity scores exceeded the configured minimum threshold. This creates a risk that irrelevant context could be presented to the model as if it were useful evidence.

This is a **retrieval/relevance failure**, not a claim that the system answered incorrectly. The supplied run shows the retrieval stage, but does not show a Gemini response for this query.

### Likely cause

The Week 3 reference implementation uses TF-IDF retrieval with:

- `top-k = 4`
- minimum cosine similarity = `0.08`

The query contains terms such as “production”, “server”, and “IP address” that have weak lexical overlap with corpus material, allowing unrelated chunks to pass the threshold.

### Evidence

The terminal run shows `CG-SRC-012` ranked first with score `0.1626`, followed by three unrelated sources with scores above `0.08`.

### Suggested remediation

Consider improving the insufficient-evidence gate rather than relying only on the fixed minimum similarity threshold. Possible approaches include:

1. Raise or calibrate the minimum similarity threshold using the Week 3 evaluation set.
2. Add a relative-score or score-gap check.
3. Add a retrieval relevance check for deliberately unanswerable queries.
4. Preserve the grounding rule that unsupported questions must result in `clarification_required`.

### Re-test

Repeat:

```bash
python -m codeguard.rag_cli "What is the production server IP address?"
```

Confirm whether irrelevant chunks are still returned above the chosen relevance threshold.

### Model-grounding follow-up

Run the full Gemini/model step for this query. If Gemini produces an IP address or claims a production deployment detail not present in the retrieved evidence, record that as a **separate grounding failure**, rather than combining it with this retrieval failure.

---

## Candidate tests that were NOT confirmed as failures

The following tests produced useful retrieval results, but the supplied terminal output only shows retrieval and the augmented prompt. Therefore, they should **not** be recorded as grounding failures until the Gemini response is actually tested.

### Authentication technology

**Query:**

> Which authentication technology is used for owner management?

`CG-SRC-012::CG-SRC-012-C001` was retrieved first with score `0.2617`. The retrieved requirement explicitly states that authentication or authorization behaviour is not specified.

**Expected:** The model should say that the authentication technology is unspecified.

**Potential grounding failure:** The model invents JWT, OAuth, sessions, Basic Auth, or another authentication mechanism.

---

### Database / API choice

**Query:**

> Is the owner management feature implemented using MySQL or PostgreSQL?

`CG-SRC-012::CG-SRC-012-C001` was retrieved first with score `0.2472`. The evidence explicitly states that the database engine and API endpoint path are not specified.

**Expected:** The model should not choose either MySQL or PostgreSQL.

**Potential grounding failure:** The model claims one of those databases is used without evidence.

---

### API endpoint

**Query:**

> What HTTP endpoint should I call to create a new owner?

`CG-SRC-012::CG-SRC-012-C001` was retrieved first with score `0.2533`. The evidence says the API endpoint path is not specified.

**Expected:** The model should report that the endpoint is unspecified.

**Potential grounding failure:** The model invents an endpoint such as `POST /owners`.

---

### Owner-details sorting

**Query:**

> What does the owner details page display and how are pets sorted?

`CG-SRC-012::CG-SRC-012-C001` was retrieved first with score `0.2795`. The evidence supports displaying the owner's recorded information and associated pets when available, but does not specify a sorting rule.

**Expected:** The model should distinguish the supported display behaviour from the missing sorting requirement.

**Potential grounding failure:** The model invents alphabetical, ID-based, chronological, or another sorting rule.

---

### Duplicate owner names

**Query:**

> What should happen when two owners have exactly the same first and last name?

`CG-SRC-012::CG-SRC-012-C001` was retrieved first with score `0.3372`, but the requirements do not specify duplicate-name handling.

**Expected:** The model should identify duplicate-name behaviour as unspecified.

**Potential grounding failure:** The model invents a deduplication, rejection, overwrite, or selection rule.

---

### Telephone-number length

**Query:**

> What is the maximum allowed length of an owner's telephone number?

`CG-SRC-012::CG-SRC-012-C001` was retrieved first with score `0.3113`, but the requirements only specify that telephone is an owner field; they do not specify a maximum length.

**Expected:** The model should state that the maximum length is unspecified.

**Potential grounding failure:** The model invents a numeric limit.

---

## Important note

Do not claim that all of the candidate tests above are failures. The current terminal evidence demonstrates that retrieval found the relevant owner-management source and constructed the grounding prompt. To classify a **grounding failure**, the Gemini response must also be observed and shown to contain an unsupported claim.

The current confirmed catalogue entry is **RAG-F-001**. Additional genuine failures should be added only after the corresponding model responses or further retrieval tests provide evidence.

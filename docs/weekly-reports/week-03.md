# Week 3 Progress Report — CodeGuard QA Agent

**Course:** BSE4104 Emerging Trends in Software Engineering  
**Week:** 3: Context Engineering and RAG  
**Week ending:** 18 September 2026  
**Group:** TEAM TO COMPLETE  
**Repository:** `codeguard-qa-agent`

## 1. Work completed against weekly objectives

The team extended the Week 2 Gemini-backed baseline with a controlled retrieval-augmented generation layer. A 12-record project corpus was assembled and registered with stable source identifiers and provenance. The corpus covers CodeGuard input/output contracts, prompt and grounding rules, RAG configuration, safety boundaries, evaluation/observability rules, the Week 2 baseline, and approved PetClinic owner-management sample requirements.

A deterministic ingestion and segmentation path was added under `src/codeguard/rag/`. Documents are loaded from the source register and divided into overlapping, line-aware chunks. A local TF-IDF index ranks chunks using cosine similarity. The retrieval layer returns source ID, chunk ID, file, original line range, and similarity score so the evidence passed to the model can be inspected.

The grounding layer constructs a clearly delimited evidence section and instructs the existing Week 2 model path to use retrieved evidence for project-specific claims, distinguish partial support, and request clarification instead of inventing missing details. The Week 2 schema validation remains the output control.

A 15-case RAG evaluation set was created with answerable, partially answerable, and deliberately unanswerable questions. Unit tests cover chunk traceability, retrieval ranking/no-evidence behavior, and visible source metadata.

## 2. Key engineering decisions

The team selected a TF-IDF retrieval index for the Week 3 reference implementation because the corpus is small, controlled, and primarily textual. The approach is local and inspectable, making ranking behavior easier to explain and reproduce. The RAG package is isolated behind `RAGPipeline`, allowing a later semantic/embedding retriever to replace the index without changing the grounding contract.

Chunks retain original line ranges and stable source IDs. This was chosen to make source grounding visible in traces rather than returning only opaque similarity results.

## 3. Challenges and failures

The principal expected retrieval limitation is lexical mismatch: a synonym-heavy query can describe the correct concept while sharing too few words with the relevant chunk. Broad or very short queries can also rank generic policy text above a more specific requirement. A third grounding risk occurs when a question is only partially supported and the model is tempted to fill the missing portion from general knowledge.

These cases are recorded in `docs/rag/failure-catalogue.md`. The team must attach genuine query/chunk/model traces and re-test evidence before marking any remediation as successful.

## 4. Evaluation/evidence status

The repository contains the 15-case evaluation definition and a runner that records retrieved sources, top score, and source-hit status. The committed results template intentionally contains `PENDING_REAL_RUN`; these placeholders must be replaced by the team's genuine run before submission. Screenshots/traces should show at least one answerable, partial, and unanswerable case plus three real failure examples.

## 5. Individual contribution summary

- **Member 1:** controlled corpus, provenance/source register, ingestion and chunking.
- **Member 2:** retrieval/indexing implementation and retrieval design.
- **Member 3:** grounding/context construction, architecture, and integration with the existing Gemini path.
- **Member 4:** 15-case evaluation assets, failure catalogue, run guide, evidence collation, and Week 3 report.

Replace the generic member labels above with the team's names/student numbers and link each contribution to the actual commit/PR and ClickUp task.

## 6. Plan for Week 4

Week 4 will retain the grounded RAG layer and introduce explicit, safe tool/function contracts. The team should define at least two approved tools, authorization/failure behavior, and human approval where a higher-impact action could occur.

## Evidence links — TEAM TO COMPLETE

- GitHub commits/PRs:
- ClickUp tasks:
- Evaluation results:
- Retrieval traces/screenshots:

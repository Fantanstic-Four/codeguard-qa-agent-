# CodeGuard QA Agent — Corpus / Source Register

**Week:** 3 — Context Engineering and RAG  
**Corpus size:** 12 controlled records  
**Policy:** Only team-created, approved sample, or otherwise authorized project material is indexed.

| ID | Source | Provenance | Purpose | Status |
|---|---|---|---|---|
| CG-SRC-001 | `knowledge/corpus/01-system-overview.md` | Team-created | Week 2 baseline/project scope | Approved |
| CG-SRC-002 | `knowledge/corpus/02-input-contract.md` | Team-created | Week 2 input behavior | Approved |
| CG-SRC-003 | `knowledge/corpus/03-output-contract.md` | Team-created | Week 2 schema/output behavior | Approved |
| CG-SRC-004 | `knowledge/corpus/04-prompt-policy.md` | Team-created | Prompt v1.1 rules | Approved |
| CG-SRC-005 | `knowledge/corpus/05-rag-retrieval-policy.md` | Team-created | Week 3 design | Approved |
| CG-SRC-006 | `knowledge/corpus/06-rag-configuration.md` | Team-created | Week 3 configuration | Approved |
| CG-SRC-007 | `knowledge/corpus/07-source-grounding.md` | Team-created | Week 3 grounding contract | Approved |
| CG-SRC-008 | `knowledge/corpus/08-safety-boundaries.md` | Team-created | Capstone boundaries adapted to project | Approved |
| CG-SRC-009 | `knowledge/corpus/09-week2-baseline.md` | Team-created | Week 2 implementation record | Approved |
| CG-SRC-010 | `knowledge/corpus/10-evaluation-policy.md` | Team-created | Week 3 evaluation design | Approved |
| CG-SRC-011 | `knowledge/corpus/11-observability.md` | Team-created | Week 3 trace design | Approved |
| CG-SRC-012 | `knowledge/corpus/12-petclinic-owner-management.md` | Team-created sample requirements | Approved sample feature requirements | Approved |

## Inclusion rules

A record is included only when the team can explain its origin and is authorized to use it. Restricted, personal, secret, or unverified external content is excluded. Each record has a stable source ID so retrieval traces and model answers can identify the evidence used.

## Change control

When a source changes materially, update the record, review its provenance, and re-run the Week 3 retrieval evaluation. Do not silently replace a source after evaluation because that would make previous evidence difficult to reproduce.

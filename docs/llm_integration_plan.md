# LLM Integration Plan

## Purpose

This document defines how LLM support will be added to the AI Novel To Script project.

The current MVP is rule-based. It can parse chapters, extract known characters, locations, events, dialogues, and generate scene-centered YAML schema version `0.2`.

Stage 3 will add AI-based extraction while keeping the current rule-based pipeline as a fallback.

---

## Design Goals

1. Keep the project runnable without an LLM API key.
2. Avoid storing API keys in the repository.
3. Separate prompt design from business logic.
4. Allow rule-based extraction and LLM-based extraction to coexist.
5. Keep the output compatible with YAML schema version `0.2`.

---

## Planned Architecture

```text
Novel Text
↓
Chapter Parser
↓
Rule-based Extractors or LLM Extractors
↓
Structured Intermediate Data
↓
Scene-Centered YAML Generator
↓
YAML Screenplay Output

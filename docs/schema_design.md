# YAML Schema Design

## Purpose

This document defines the YAML schema used by the AI Novel To Script system.

The goal is to transform long-form novels into structured screenplay representations that can be further edited, visualized, or converted into storyboards.

---

## Design Principles

1. Human-readable
2. Easy for AI generation
3. Easy for future expansion
4. Compatible with screenplay workflows

---

## Top-Level Structure

```yaml
metadata:
characters:
locations:
scenes:
```

---

## Character Schema

```yaml
characters:
  - id: char_001
    name: Lin Fan
    role: protagonist
```

---

## Location Schema

```yaml
locations:
  - id: loc_001
    name: QingShan Town
```

---

## Scene Schema

```yaml
scenes:
  - scene_id: scene_001

    location: loc_001

    participants:
      - char_001

    summary: >
      Lin Fan decides to leave his hometown.

    dialogues:
      - speaker: Lin Fan
        content: I want to leave this place.
```

---

## Future Extensions

- Character relationships
- Story timeline
- Emotion analysis
- Storyboard generation

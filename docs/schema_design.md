# YAML Schema Design

## Purpose

This document defines the YAML schema used by the AI Novel To Script system.

The goal is to convert long-form novels into structured screenplay data that can be edited, visualized, or further transformed into storyboards and video-generation prompts.

---

## Schema Design Direction

The current schema uses a scene-centered structure.

A screenplay is not only a list of characters, locations, events, and dialogues. In practice, the most important unit is the scene.

Each scene should describe:

- where the scene happens
- which characters appear
- what happens in the scene
- what actions are visible
- what dialogues are spoken
- what emotional or dramatic purpose the scene serves

Therefore, this project uses global catalogs for reusable entities and scene-level structures for actual screenplay content.

---

## Top-Level Structure

```yaml
metadata:
characters:
locations:
scenes:
```

---

## Metadata Schema

```yaml
metadata:
  schema_version: "0.2"
  project_name: "AI Novel To Script"
  source_type: "novel"
  language: "zh-CN"
  chapter_count: 3
  character_count: 4
  location_count: 5
  scene_count: 3
```

### Design Reason

The metadata section records basic information about the generated script.

`schema_version` is included so that future versions can change the YAML format without breaking compatibility.

---

## Character Schema

```yaml
characters:
  - id: char_001
    name: 林凡
    role: protagonist
    description: "A young man who leaves his village to search for the truth."
    first_appearance: scene_001
```

### Field Explanation

| Field | Meaning |
| --- | --- |
| id | Stable internal character ID |
| name | Character display name |
| role | Narrative role, such as protagonist or supporting character |
| description | Short character description |
| first_appearance | First scene where the character appears |

### Design Reason

Characters are stored as reusable global entities.

Scenes can refer to characters through their IDs instead of repeating full character information.

---

## Location Schema

```yaml
locations:
  - id: loc_001
    name: 青山村
    description: "A quiet village where the story begins."
```

### Field Explanation

| Field | Meaning |
| --- | --- |
| id | Stable internal location ID |
| name | Location display name |
| description | Short location description |

### Design Reason

Locations are stored separately because the same location may appear in multiple scenes.

This also supports future extensions such as maps, story timelines, or visual background generation.

---

## Scene Schema

```yaml
scenes:
  - id: scene_001
    chapter: 1
    title: "第一章 初醒"
    location: loc_001

    participants:
      - char_001
      - char_002

    summary: "林凡醒来后，从王叔那里得知父亲留下了一封重要的信。"

    dramatic_purpose: "Introduce the protagonist and trigger the main mystery."

    actions:
      - actor: char_001
        description: "林凡从破旧的木床上醒来。"
      - actor: char_002
        description: "王叔站在门口，手里拿着一封泛黄的信。"

    events:
      - id: event_001
        type: wake_up
        description: "林凡醒来。"
      - id: event_002
        type: receive_letter
        description: "王叔把父亲留下的信交给林凡。"

    dialogues:
      - id: dialogue_001
        speaker: char_002
        content: "你父亲留下的东西，到了该交给你的时候。"
```

### Field Explanation

| Field | Meaning |
| --- | --- |
| id | Stable scene ID |
| chapter | Source chapter number |
| title | Scene title |
| location | Location ID |
| participants | Character IDs appearing in the scene |
| summary | Short scene summary |
| dramatic_purpose | Narrative function of the scene |
| actions | Visible actions that can support storyboard generation |
| events | Key story events in the scene |
| dialogues | Dialogue lines spoken in the scene |

### Design Reason

The scene is the central unit of the screenplay.

This structure is useful because future modules can generate:

- storyboard panels from actions
- character prompts from participants
- background prompts from locations
- video clips from scene-level descriptions
- dialogue subtitles from dialogue entries

---

## Example Output

```yaml
metadata:
  schema_version: "0.2"
  project_name: "AI Novel To Script"
  source_type: "novel"
  language: "zh-CN"
  chapter_count: 3
  character_count: 4
  location_count: 5
  scene_count: 3

characters:
  - id: char_001
    name: 林凡
    role: protagonist
    description: "A young man searching for the truth."
    first_appearance: scene_001

  - id: char_002
    name: 王叔
    role: supporting
    description: "An older man who gives Lin Fan an important letter."
    first_appearance: scene_001

locations:
  - id: loc_001
    name: 青山村
    description: "The village where the story begins."

scenes:
  - id: scene_001
    chapter: 1
    title: "第一章 初醒"
    location: loc_001
    participants:
      - char_001
      - char_002
    summary: "林凡醒来后，从王叔那里得知父亲留下了一封重要的信。"
    dramatic_purpose: "Trigger the protagonist's journey."
    actions:
      - actor: char_001
        description: "林凡从破旧的木床上醒来。"
      - actor: char_002
        description: "王叔站在门口，手里拿着一封泛黄的信。"
    events:
      - id: event_001
        type: wake_up
        description: "林凡醒来。"
      - id: event_002
        type: receive_letter
        description: "王叔把父亲留下的信交给林凡。"
    dialogues:
      - id: dialogue_001
        speaker: char_002
        content: "你父亲留下的东西，到了该交给你的时候。"
```

---

## Future Extensions

The schema can be extended with:

- emotion tags
- camera shot suggestions
- storyboard prompts
- image generation prompts
- scene duration estimation
- character relationship graph
- timeline visualization

---

## Current Version

Schema version: `0.2`

This version focuses on scene-centered screenplay structure.

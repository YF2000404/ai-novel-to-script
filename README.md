# AI Novel To Script

## Project Overview

An AI-assisted screenplay generation tool that converts long-form novels into structured YAML scripts.

The system aims to help authors quickly transform novels into editable screenplay drafts.

---

## Features

- Novel chapter parsing
- Character extraction
- Scene extraction
- Event extraction
- Dialogue extraction
- YAML screenplay generation

---

## Development Roadmap

### Phase 1

- [ ] Design YAML Schema
- [ ] Define screenplay data structure

### Phase 2

- [ ] Chapter segmentation
- [ ] Character extraction

### Phase 3

- [ ] Scene extraction
- [ ] Event extraction

### Phase 4

- [ ] YAML generation

### Phase 5

- [ ] Frontend visualization

---

## Repository Structure

```
docs/
src/
tests/
sample_data/
```

---

## Tech Stack

- Python
- OpenAI Compatible LLM
- YAML
- GitHub

## Current Prototype

The current prototype supports a rule-based novel-to-screenplay pipeline using YAML schema version `0.2`.

```text
Sample Novel
↓
Chapter Parser
↓
Character Extractor
↓
Location Extractor
↓
Event Extractor
↓
Dialogue Extractor
↓
Scene Extractor
↓
Scene-Centered YAML Generator
↓
YAML Screenplay Output
```

This version does not use an external LLM yet. It focuses on building a clear, testable, and extensible software structure first.

---

## YAML Schema Version

Current schema version:

```text
0.2
```

The current YAML output uses a scene-centered screenplay structure.

Instead of only listing characters, locations, events, and dialogues separately, the output organizes screenplay content around scenes.

Each scene may include:

- source chapter number
- scene title
- location reference
- participating characters
- scene summary
- dramatic purpose
- visible actions
- scene-level events
- scene-level dialogues

This structure is designed to support future storyboard generation, image generation prompts, and AI video generation workflows.

---

## How to Run

Install dependencies with:

```bash
pip install -r requirements.txt
```

Run the full conversion pipeline with:

```bash
python src/run_pipeline.py
```

Run tests with:

```bash
pytest
```

The generated YAML output will be written to:

```text
sample_data/output_script.yaml
```

This generated file is ignored by Git because it is produced by running the pipeline.

## Repository Structure

```text
docs/
  schema_design.md
  system_design.md

src/
  chapter_parser.py
  character_extractor.py
  scene_extractor.py
  yaml_generator.py
  run_parser_demo.py
  run_pipeline.py

tests/
  test_chapter_parser.py
  test_character_extractor.py
  test_scene_extractor.py
  test_yaml_generator.py

sample_data/
  sample_novel.txt
```

---

## How to Run

Run the basic pipeline with:

```bash
python src/run_pipeline.py
```

The pipeline reads:

```text
sample_data/sample_novel.txt
```

and generates:

```text
sample_data/output_script.yaml
```

---

## Current Features

- Split Chinese novel text into chapters
- Extract basic character information
- Extract basic scene information
- Generate structured YAML screenplay output
- Provide basic unit tests for core modules

---

## Future Plan

- Improve character extraction with LLM support
- Add location extraction
- Add event extraction
- Add dialogue extraction
- Build a web interface for uploading novels and downloading YAML scripts

## Development Setup

Install dependencies with:

```bash
pip install -r requirements.txt
```

Run the basic conversion pipeline with:

```bash
python src/run_pipeline.py
```

Run tests with:

```bash
pytest
```

The generated YAML output will be written to:

```text
sample_data/output_script.yaml
```

This generated file is ignored by Git because it is produced by running the pipeline.

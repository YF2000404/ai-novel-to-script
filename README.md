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

The current prototype supports a basic rule-based pipeline:

```text
Sample Novel
↓
Chapter Parser
↓
Character Extractor
↓
Scene Extractor
↓
YAML Generator
↓
YAML Output
```

This version does not use an external LLM yet. It focuses on building a clear and testable software structure first.

---

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

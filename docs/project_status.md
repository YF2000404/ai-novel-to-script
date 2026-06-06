# Project Status

## Project Name

AI Novel To Script

## Current Version

Rule-based MVP Prototype

---

## Completed Features

- GitHub repository setup
- README initialization
- YAML schema design document
- System design document
- Basic project structure
- Chapter parser
- Character extractor
- Location extractor
- Event extractor
- Dialogue extractor
- Scene extractor
- YAML generator
- Basic end-to-end pipeline
- Unit tests for core modules
- Sample Chinese novel input

---

## Current Pipeline

```text
sample_data/sample_novel.txt
↓
split_chapters()
↓
extract_characters()
↓
extract_locations()
↓
extract_events()
↓
extract_dialogues()
↓
extract_scenes()
↓
generate_yaml()
↓
sample_data/output_script.yaml
```

---

## Current Output Structure

The current YAML output uses schema version `0.2`.

The output contains:

- metadata
- characters
- locations
- scenes

Each scene contains:

- chapter number
- title
- location reference
- participants
- summary
- dramatic purpose
- actions
- events
- dialogues

---

## Current Limitations

- Rule-based extraction only
- Character extraction relies on a fixed name list
- Location extraction relies on a fixed location list
- Event extraction relies on keyword rules
- Dialogue extraction only supports Chinese quotation marks
- Scene extraction currently treats each chapter as one scene
- No LLM support yet
- No web interface yet
- YAML schema is still basic

---

## Current Engineering Status

The current MVP has a complete rule-based pipeline and basic unit tests.

The project can be tested with:

```bash
pytest

---

## Next Development Stages

### Stage 1: Stabilize MVP

Status: Completed

Completed items:

- Added `.gitignore`
- Added `requirements.txt`
- Added README setup and test instructions
- Added basic pipeline test

### Stage 2: Improve YAML Schema

Status: Completed

Completed items:

- Updated `docs/schema_design.md` with scene-centered schema version `0.2`
- Added schema version metadata
- Updated YAML generator to produce scene-centered screenplay output
- Added character role, description, and first appearance fields
- Added location descriptions
- Moved events and dialogues into scene-level structures
- Added participants, actions, and dramatic purpose under each scene
- Updated YAML generator tests
- Updated pipeline test for schema version `0.2`
- Updated README with schema version `0.2` explanation

### Stage 3: Add LLM Support

- Add LLM client module
- Add prompt templates
- Add AI-based extraction option
- Add fallback to rule-based extraction

### Stage 4: Build Web Interface

- Add upload interface
- Add conversion button
- Display YAML result
- Add YAML download

### Stage 5: Final Submission

- Polish README
- Add demo video link
- Add screenshots
- Add final project explanation

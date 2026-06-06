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

Status: Completed

Completed items:

- Added `docs/llm_integration_plan.md`
- Added `src/prompt_templates.py`
- Added prompt template tests
- Added `src/llm_client.py`
- Added `MockLLMClient`
- Added `RealLLMClient` skeleton
- Added `.env.example`
- Added AI character extractor
- Added AI location extractor
- Added AI event extractor
- Added AI dialogue extractor
- Added tests for all AI extractors
- Added AI pipeline script
- Added AI pipeline test
- Added extraction mode selector
- Added tests for extraction mode selector
- Updated README with unified pipeline instructions
- Kept rule-based extraction as the default fallback mode

Current extraction modes:

```text
rule -> local rule-based extraction
ai   -> mock LLM-based extraction

### Stage 4: Build Web Interface

Status: Completed

Completed items:

- Added `docs/web_interface_plan.md`
- Added Flask dependency
- Added `src/web_app.py`
- Added `templates/index.html`
- Added `static/style.css`
- Added novel text input area
- Added extraction mode selector
- Added YAML conversion button
- Added generated YAML display area
- Added YAML download support
- Added Flask web app tests
- Updated README with web interface instructions

Current web app command:

```bash
python src/web_app.py

### Stage 5: Final Submission

Status: Ready to Start

Planned items:

- Polish README
- Add screenshots
- Add demo video link
- Add final project explanation
- Verify all tests pass
- Verify web app can run locally
- Verify GitHub PR history is clear
- Verify repository is publicly accessible

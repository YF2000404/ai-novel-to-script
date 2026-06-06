# AI Novel To Script

## Project Overview

AI Novel To Script is an AI-assisted screenplay generation tool that converts long-form Chinese novels into structured YAML screenplay data.

The project is designed as the first step of an AI comic/video generation workflow:

```text
Novel
↓
Structured Screenplay YAML
↓
Storyboard
↓
Image Generation
↓
Video Generation
```

The current version focuses on converting novel text into scene-centered screenplay YAML.

---

## 中文简介

本项目用于将中文长篇小说自动转换为结构化 YAML 剧本。

当前版本已经支持：

- 小说章节切分
- 人物提取
- 地点提取
- 事件提取
- 对白提取
- 场景提取
- Scene-centered YAML 剧本生成
- Rule-based extraction mode
- Mock LLM-based AI extraction mode
- 基础单元测试与 pipeline 测试

---

## Current Status

Current project version:

```text
Rule-based MVP + Mock LLM AI Pipeline
```

Current YAML schema version:

```text
0.2
```

Current main pipeline entry point:

```bash
python src/run_pipeline.py
```

The project currently supports two extraction modes:

```text
rule  -> local rule-based extraction
ai    -> mock LLM-based extraction
```

The default mode is:

```text
rule
```

---

## Key Features

### 1. Chapter Parsing

The chapter parser splits Chinese novel text into chapters.

Supported chapter title examples:

```text
第一章
第二章
第1章
第十二章
```

---

### 2. Rule-based Extraction

The rule-based pipeline can extract:

- characters
- locations
- events
- dialogues
- scenes

This mode does not require any LLM API key.

---

### 3. Mock LLM-based AI Extraction

The AI pipeline currently uses a mock LLM client.

It simulates LLM responses for:

- character extraction
- location extraction
- event extraction
- dialogue extraction

This allows the AI extraction architecture to be tested without requiring network access or a real API key.

---

### 4. Scene-centered YAML Output

The generated YAML uses schema version `0.2`.

Instead of only listing characters, locations, events, and dialogues separately, the current schema organizes screenplay content around scenes.

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

## System Pipeline

### Unified Pipeline

```text
Sample Novel
↓
Chapter Parser
↓
Extraction Mode Selector
↓
Rule-based Extractors or AI Extractors
↓
Scene Extractor
↓
Scene-centered YAML Generator
↓
YAML Screenplay Output
```

---

## Run Rule-based Pipeline

Rule-based mode is the default mode.

```bash
python src/run_pipeline.py
```

This mode uses local rule-based extractors:

```text
character_extractor.py
location_extractor.py
event_extractor.py
dialogue_extractor.py
```

## Web Interface

The project now includes a simple Flask web interface for demo usage.

The web interface allows users to:

- paste Chinese novel text
- choose extraction mode
- convert the novel into scene-centered YAML
- view the generated YAML result
- download the YAML file

---

## Run Web App

Install dependencies first:

```bash
pip install -r requirements.txt
```

Start the Flask web app:

```bash
python src/web_app.py
```

Then open the following address in a browser:

```text
http://127.0.0.1:5000
```

---

## Web App Workflow

```text
Open Web Page
↓
Paste Novel Text
↓
Choose Extraction Mode
↓
Click Convert to YAML
↓
View Generated YAML
↓
Download YAML
```

---

## Supported Web Extraction Modes

The web interface supports the same extraction modes as the command-line pipeline:

```text
rule -> local rule-based extraction
ai   -> mock LLM-based extraction
```

The default mode is:

```text
rule
```

The AI mode currently uses `MockLLMClient`, so no real API key is required.
---

## Run AI Pipeline

The AI mode currently uses `MockLLMClient`.

On macOS/Linux:

```bash
EXTRACTION_MODE=ai python src/run_pipeline.py
```

On Windows PowerShell:

```powershell
$env:EXTRACTION_MODE="ai"
python src/run_pipeline.py
```

The current AI mode does not require a real API key.

---

## LLM Configuration

The current default LLM mode is:

```text
LLM_MODE=mock
```

A real LLM client skeleton is included, but real API calls are not enabled yet.

Future real LLM configuration should use environment variables:

```text
LLM_API_KEY
LLM_BASE_URL
LLM_MODEL
```

Real API keys must never be committed to GitHub.

An example configuration file is provided:

```text
.env.example
```

---

## Output

The pipeline reads:

```text
sample_data/sample_novel.txt
```

The unified pipeline writes generated YAML to:

```text
sample_data/output_script.yaml
```

This generated output file is ignored by Git.

The older AI demo script may also generate:

```text
sample_data/output_ai_script.yaml
```

This file is also ignored by Git.

---

## YAML Schema Version

Current schema version:

```text
0.2
```

Top-level YAML structure:

```yaml
metadata:
characters:
locations:
scenes:
```

Example scene-centered structure:

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

    dramatic_purpose: "Trigger the protagonist's journey."

    actions:
      - actor: unknown
        description: "林凡从破旧的木床上醒来。"

    events:
      - id: event_001
        type: wake_up
        description: "林凡醒来。"

    dialogues:
      - id: dialogue_001
        speaker: 王叔
        content: "你父亲留下的东西，到了该交给你的时候。"
```

For the full schema design, see:

```text
docs/schema_design.md
```

---

## Repository Structure

```text
docs/
  schema_design.md
  system_design.md
  project_status.md
  llm_integration_plan.md

src/
  chapter_parser.py
  character_extractor.py
  location_extractor.py
  event_extractor.py
  dialogue_extractor.py
  scene_extractor.py
  yaml_generator.py

  prompt_templates.py
  llm_client.py
  ai_character_extractor.py
  ai_location_extractor.py
  ai_event_extractor.py
  ai_dialogue_extractor.py

  extraction_mode.py
  run_parser_demo.py
  run_pipeline.py
  run_ai_pipeline.py

tests/
  test_chapter_parser.py
  test_character_extractor.py
  test_location_extractor.py
  test_event_extractor.py
  test_dialogue_extractor.py
  test_scene_extractor.py
  test_yaml_generator.py
  test_pipeline.py

  test_prompt_templates.py
  test_llm_client.py
  test_ai_character_extractor.py
  test_ai_location_extractor.py
  test_ai_event_extractor.py
  test_ai_dialogue_extractor.py
  test_ai_pipeline.py
  test_extraction_mode.py

sample_data/
  sample_novel.txt

.env.example
.gitignore
requirements.txt
README.md
```

---

## Development Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

Run the default rule-based pipeline:

```bash
python src/run_pipeline.py
```

Run the mock LLM AI pipeline:

```bash
EXTRACTION_MODE=ai python src/run_pipeline.py
```

On Windows PowerShell:

```powershell
$env:EXTRACTION_MODE="ai"
python src/run_pipeline.py
```

---

## Tech Stack

- Python
- YAML
- Regular expressions
- Mock LLM client
- Environment-variable based configuration
- Pytest
- GitHub Pull Request workflow

---

## Current Limitations

The current version is still an MVP.

Known limitations:

- Rule-based extraction has limited generalization ability.
- AI mode currently uses mock LLM responses only.
- Real LLM API calls are not implemented yet.
- Scene extraction currently treats each chapter as one scene.
- Character and location matching are still simple.
- No web interface yet.
- No direct storyboard or video generation yet.

---

## Development Roadmap

### Stage 1: Stabilize MVP

Status: Completed

Completed items:

- Added `.gitignore`
- Added `requirements.txt`
- Added README setup and test instructions
- Added basic pipeline test

---

### Stage 2: Improve YAML Schema

Status: Completed

Completed items:

- Added scene-centered YAML schema version `0.2`
- Added schema version metadata
- Updated YAML generator to produce scene-centered screenplay output
- Added character role, description, and first appearance fields
- Added location descriptions
- Moved events and dialogues into scene-level structures
- Added participants, actions, and dramatic purpose under each scene
- Updated YAML generator tests
- Updated pipeline test for schema version `0.2`

---

### Stage 3: Add LLM Support

Status: In Progress

Completed items:

- Added LLM integration plan
- Added prompt templates
- Added mock LLM client
- Added real LLM client skeleton
- Added AI character extractor
- Added AI location extractor
- Added AI event extractor
- Added AI dialogue extractor
- Added AI pipeline test
- Added extraction mode selector
- Added tests for extraction mode selector
- Added `.env.example`

Remaining items:

- Update project status document
- Polish Stage 3 documentation
- Optionally implement real API call support later

---

### Stage 4: Build Web Interface

Status: Not Started

Planned items:

- Add file upload interface
- Add conversion button
- Display generated YAML
- Add YAML download feature
- Prepare demo-friendly UI

---

### Stage 5: Final Submission

Status: Not Started

Planned items:

- Polish README
- Add screenshots
- Add demo video link
- Add final project explanation
- Verify all PR and commit history
- Verify repository is publicly accessible

---

## Submission Notes

This repository is developed using a continuous Pull Request workflow.

Each feature is added through small PRs with clear descriptions, including:

- feature purpose
- implementation details
- testing method

This follows the competition requirement that development should be continuous rather than submitted only at the end.

---

## Future Extensions

Planned future improvements:

- Real LLM API integration
- Better JSON validation for LLM output
- More accurate scene segmentation
- Character relationship graph
- Timeline visualization
- Storyboard prompt generation
- Image generation prompt generation
- Web-based upload and download interface

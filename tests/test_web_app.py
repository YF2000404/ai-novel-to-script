"""
Tests for Flask web app.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from web_app import app


def test_web_app_home_page_loads():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    assert b"AI Novel To Script" in response.data
    assert b"Convert to YAML" in response.data


def test_web_app_empty_input_shows_error():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.post("/", data={
            "novel_text": "",
            "extraction_mode": "rule"
        })

    assert response.status_code == 200
    assert b"Please enter novel text before conversion." in response.data


def test_web_app_rule_conversion_displays_yaml():
    app.config["TESTING"] = True

    novel_text = """
第一章 初醒

林凡从床上醒来，王叔站在门口。
王叔说：“你父亲留下的东西，到了该交给你的时候。”
"""

    with app.test_client() as client:
        response = client.post("/", data={
            "novel_text": novel_text,
            "extraction_mode": "rule"
        })

    assert response.status_code == 200
    assert b"Generated YAML" in response.data
    assert b"metadata:" in response.data
    assert b"schema_version" in response.data
    assert b"characters:" in response.data
    assert b"scenes:" in response.data


def test_web_app_ai_conversion_displays_yaml():
    app.config["TESTING"] = True

    novel_text = """
第一章 初醒

林凡从床上醒来，王叔站在门口。
"""

    with app.test_client() as client:
        response = client.post("/", data={
            "novel_text": novel_text,
            "extraction_mode": "ai"
        })

    assert response.status_code == 200
    assert b"Generated YAML" in response.data
    assert b"metadata:" in response.data
    assert b"schema_version" in response.data
    assert b"characters:" in response.data
    assert b"scenes:" in response.data


def test_download_yaml_success():
    app.config["TESTING"] = True

    novel_text = """
第一章 初醒

林凡从床上醒来，王叔站在门口。
"""

    with app.test_client() as client:
        response = client.post("/download", data={
            "novel_text": novel_text,
            "extraction_mode": "rule"
        })

    assert response.status_code == 200
    assert response.mimetype == "text/yaml"
    assert "attachment; filename=script_output.yaml" in (
        response.headers["Content-Disposition"]
    )
    assert b"metadata:" in response.data
    assert b"scenes:" in response.data


def test_download_yaml_empty_input_returns_error():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.post("/download", data={
            "novel_text": "",
            "extraction_mode": "rule"
        })

    assert response.status_code == 400
    assert b"Please enter novel text before downloading YAML." in response.data

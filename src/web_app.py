"""
Basic Flask web app for AI Novel To Script.

This web app allows users to paste novel text, choose an extraction mode,
generate scene-centered YAML output, and download the YAML file.
"""

from flask import Flask
from flask import Response
from flask import render_template
from flask import request

from chapter_parser import split_chapters
from extraction_mode import run_extraction
from scene_extractor import extract_scenes
from yaml_generator import generate_yaml


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


def convert_novel_to_yaml(novel_text, selected_mode):
    """
    Convert novel text into scene-centered YAML output.
    """
    chapters = split_chapters(novel_text)
    extraction_result = run_extraction(chapters, mode=selected_mode)
    scenes = extract_scenes(chapters)

    yaml_output = generate_yaml(
        chapters,
        extraction_result["characters"],
        extraction_result["locations"],
        extraction_result["events"],
        extraction_result["dialogues"],
        scenes
    )

    return yaml_output


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Render the main web page and handle conversion requests.
    """
    yaml_output = ""
    novel_text = ""
    selected_mode = "rule"
    error_message = ""

    if request.method == "POST":
        novel_text = request.form.get("novel_text", "")
        selected_mode = request.form.get("extraction_mode", "rule")

        if not novel_text.strip():
            error_message = "Please enter novel text before conversion."
        else:
            try:
                yaml_output = convert_novel_to_yaml(
                    novel_text,
                    selected_mode
                )
            except RuntimeError as error:
                error_message = str(error)

    return render_template(
        "index.html",
        novel_text=novel_text,
        selected_mode=selected_mode,
        yaml_output=yaml_output,
        error_message=error_message
    )


@app.route("/download", methods=["POST"])
def download_yaml():
    """
    Generate and download YAML output.
    """
    novel_text = request.form.get("novel_text", "")
    selected_mode = request.form.get("extraction_mode", "rule")

    if not novel_text.strip():
        return Response(
            "Please enter novel text before downloading YAML.",
            status=400,
            mimetype="text/plain"
        )

    try:
        yaml_output = convert_novel_to_yaml(novel_text, selected_mode)
    except RuntimeError as error:
        return Response(
            str(error),
            status=400,
            mimetype="text/plain"
        )

    return Response(
        yaml_output,
        mimetype="text/yaml",
        headers={
            "Content-Disposition": "attachment; filename=script_output.yaml"
        }
    )


if __name__ == "__main__":
    app.run(debug=True)

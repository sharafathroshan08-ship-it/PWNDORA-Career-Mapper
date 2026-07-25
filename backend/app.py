from flask import Flask, request, jsonify
from flask_cors import CORS
import tempfile
import os

from pdf_reader import extract_text_from_pdf
from parser import run_parser
from mapper import run_mapper
from role_mapper import run_role_mapper
from gap_analysis import run_gap_analysis
from learning_path import run_learning_path

app = Flask(__name__)

# Allow frontend requests
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "application": "PWNDORA Career Mapper",
        "version": "1.0"
    })


@app.route("/analyze", methods=["POST"])
def analyze_resume():

    if "resume" not in request.files:
        return jsonify({
            "success": False,
            "message": "No resume uploaded."
        }), 400

    resume_file = request.files["resume"]

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    try:

        resume_file.save(temp_file.name)

        resume_text = extract_text_from_pdf(temp_file.name)

        if resume_text.strip() == "":
            return jsonify({
                "success": False,
                "message": "Unable to extract text from PDF."
            }), 400

        parsed = run_parser(resume_text)

        mapping = run_mapper()

        roles = run_role_mapper()

        gaps = run_gap_analysis()

        learning = run_learning_path()

        return jsonify({

            "success": True,

            "parsed_resume": parsed,

            "mapping_result": mapping,

            "recommended_roles": roles,

            "gap_analysis": gaps,

            "learning_path": learning

        })

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        }), 500

    finally:

        temp_file.close()

        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
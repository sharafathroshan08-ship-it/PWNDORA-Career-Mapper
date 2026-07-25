from flask import Flask, request, jsonify
from flask_cors import CORS
import tempfile
import os

from backend.pdf_reader import extract_text_from_pdf
from backend.parser import run_parser
from backend.mapper import run_mapper
from backend.role_mapper import run_role_mapper
from backend.gap_analysis import run_gap_analysis
from backend.learning_path import run_learning_path

from backend.analytics import generate_dashboard_statistics
from backend.ai_engine import generate_ai_summary
from backend.roadmap_engine import generate_learning_roadmap
from backend.report_generator import generate_final_report

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "application": "PWNDORA AI",
        "version": "2.0"
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

        # -------------------------
        # Existing PWNDORA Pipeline
        # -------------------------

        parsed = run_parser(resume_text)

        mapping = run_mapper()

        roles = run_role_mapper()

        gaps = run_gap_analysis()

        learning = run_learning_path()

        # -------------------------
        # PWNDORA AI v2
        # -------------------------

        analytics = generate_dashboard_statistics(
            mapping,
            parsed
        )

        ai_summary = generate_ai_summary(
            mapping,
            parsed
        )

        roadmap = generate_learning_roadmap(
            gaps
        )

        report = generate_final_report(
            parsed_resume=parsed,
            mapping_result=mapping,
            recommended_roles=roles,
            gap_analysis=gaps,
            learning_path=learning,
            analytics=analytics,
            ai_summary=ai_summary,
            roadmap=roadmap
        )

        return jsonify({

            "success": True,

            "parsed_resume": parsed,

            "mapping_result": mapping,

            "recommended_roles": roles,

            "gap_analysis": gaps,

            "learning_path": learning,

            "analytics": analytics,

            "ai_summary": ai_summary,

            "roadmap": roadmap,

            "report": report

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
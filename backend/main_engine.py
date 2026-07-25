import json
import os

from pdf_reader import extract_text_from_pdf
from parser import run_parser
from mapper import run_mapper
from role_mapper import run_role_mapper
from gap_analysis import run_gap_analysis
from learning_path import run_learning_path

print("=" * 60)
print("PWNDORA CAREER MAPPER")
print("=" * 60)

print("\nSTEP 1 : Resume Upload")
pdf_path = input("Enter Resume PDF Path : ")

resume = extract_text_from_pdf(pdf_path)

print("\nResume Successfully Extracted!")

print("\nSTEP 2 : Resume Parsing")
parsed = run_parser(resume)

print("\nSTEP 3 : Domain Mapping")
mapping = run_mapper()

print("\nSTEP 4 : Role Recommendation")
roles = run_role_mapper()

print("\nSTEP 5 : Gap Analysis")
gaps = run_gap_analysis()

print("\nSTEP 6 : Learning Path")
labs = run_learning_path()

report = {
    "parsed_resume": parsed,
    "mapping_result": mapping,
    "recommended_roles": roles,
    "gap_analysis": gaps,
    "learning_path": labs
}

os.makedirs("output", exist_ok=True)

with open("output/final_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4)

print("\n" + "=" * 60)
print("PWNDORA ANALYSIS COMPLETED")
print("=" * 60)
print("Report saved to output/final_report.json")
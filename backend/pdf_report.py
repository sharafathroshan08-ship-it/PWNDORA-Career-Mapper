from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)


styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.textColor = colors.HexColor("#0077cc")

heading_style = styles["Heading2"]
heading_style.textColor = colors.HexColor("#005599")

normal_style = styles["BodyText"]


def generate_pdf_report(report, output_path):

    doc = SimpleDocTemplate(output_path)

    elements = []

    elements.append(
        Paragraph(
            "PWNDORA AI Career Report",
            title_style
        )
    )

    elements.append(Spacer(1, 0.3 * inch))
        # ==================================================
    # ANALYTICS
    # ==================================================

    analytics = report.get("analytics", {})
    ai_summary = report.get("ai_summary", {})

    elements.append(
        Paragraph(
            "Career Overview",
            heading_style
        )
    )

    overview_data = [

        ["Career Readiness", f"{analytics.get('career_readiness',0)}%"],

        ["Skill Coverage", f"{analytics.get('skill_coverage',0)}%"],

        ["Matched Skills", str(analytics.get("matched_skills",0))],

        ["Matched Tools", str(analytics.get("matched_tools",0))],

        ["Matched Certificates", str(analytics.get("matched_certificates",0))],

        ["Readiness Level", ai_summary.get("readiness_level","N/A")]

    ]

    table = Table(
        overview_data,
        colWidths=[220,220]
    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0077cc")),

            ("TEXTCOLOR",(0,0),(-1,-1),colors.black),

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#dceeff")),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8),

            ("FONTNAME",(0,0),(-1,-1),"Helvetica")

        ])

    )

    elements.append(table)

    elements.append(Spacer(1,0.25*inch))

    # ==================================================
    # AI SUMMARY
    # ==================================================

    elements.append(

        Paragraph(

            "AI Recommendation",

            heading_style

        )

    )

    elements.append(

        Paragraph(

            ai_summary.get(

                "recommendation",

                "No recommendation generated."

            ),

            normal_style

        )

    )

    elements.append(Spacer(1,0.30*inch))
        # ==================================================
    # DOMAIN SCORES
    # ==================================================

    elements.append(
        Paragraph(
            "Cybersecurity Domain Scores",
            heading_style
        )
    )

    domain_rows = [["Domain", "Score"]]

    for item in report["mapping_result"]["domain_scores"]:

        domain_rows.append([
            item["domain"],
            str(item["score"])
        ])

    domain_table = Table(domain_rows, colWidths=[300,120])

    domain_table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0077cc")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("GRID",(0,0),(-1,-1),1,colors.grey),
        ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),
        ("BOTTOMPADDING",(0,0),(-1,-1),8)
    ]))

    elements.append(domain_table)

    elements.append(Spacer(1,0.30*inch))

    # ==================================================
    # RECOMMENDED ROLES
    # ==================================================

    elements.append(
        Paragraph(
            "Recommended Career Roles",
            heading_style
        )
    )

    role_rows = [["Role", "Score"]]

    for role in report["recommended_roles"]:

        role_rows.append([
            role["role"],
            str(role["score"])
        ])

    role_table = Table(role_rows, colWidths=[300,120])

    role_table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0077cc")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("GRID",(0,0),(-1,-1),1,colors.grey),
        ("BACKGROUND",(0,1),(-1,-1),colors.beige)
    ]))

    elements.append(role_table)

    elements.append(Spacer(1,0.30*inch))

    # ==================================================
    # GAP ANALYSIS
    # ==================================================

    elements.append(
        Paragraph(
            "Top Skill Gaps",
            heading_style
        )
    )

    gap_rows = [["Skill", "Priority"]]

    for gap in report["gap_analysis"][:10]:

        gap_rows.append([
            gap["skill"],
            gap["priority"]
        ])

    gap_table = Table(gap_rows, colWidths=[300,120])

    gap_table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0077cc")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("GRID",(0,0),(-1,-1),1,colors.grey),
        ("BACKGROUND",(0,1),(-1,-1),colors.lightgrey)
    ]))

    elements.append(gap_table)

    elements.append(Spacer(1,0.30*inch))

    # ==================================================
    # FOOTER
    # ==================================================

    elements.append(
        Paragraph(
            "<b>Generated by PWNDORA AI Career Mapper</b>",
            title_style
        )
    )

    doc.build(elements)

    return output_path
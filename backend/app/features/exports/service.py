from io import BytesIO

from datetime import datetime
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
)


TEAL = colors.HexColor("#00F5D4")
MAGENTA = colors.HexColor("#FF007F")
PURPLE = colors.HexColor("#9400D3")

NAVY = colors.HexColor("#081024")
NAVY_2 = colors.HexColor("#10183B")

DARK_TEXT = colors.HexColor("#161A2B")
MUTED = colors.HexColor("#667085")
LIGHT_BG = colors.HexColor("#F5F7FB")
BORDER = colors.HexColor("#D9E0EB")
WHITE = colors.white


def _safe(value, fallback="—"):
    if value is None:
        return fallback

    value = str(value).strip()

    return value or fallback


def _escape_text(value):
    return escape(_safe(value))


def _html_text(value):
    return _escape_text(value).replace("\n", "<br/>")


def _bullet_lines(items):
    if not items:
        return "—"

    return "<br/>".join(
        f"• {_escape_text(item)}"
        for item in items
    )


def _format_created_at(value):
    if not value:
        return ""

    try:
        parsed = datetime.fromisoformat(
            value.replace("Z", "+00:00")
        )

        return parsed.strftime("%b %d, %Y • %I:%M %p")

    except (ValueError, AttributeError):
        return str(value)


def _result_sections(tool_id: str, result: dict):
    if tool_id == "clarity":
        return [
            ("Clarity Score", f"{result.get('score', '—')}/100"),
            ("Status", result.get("label")),
            ("Recommendation", result.get("recommendation")),
            ("Refined Executive Copy", result.get("refined_text")),
        ]

    if tool_id == "kpi-cleaner":
        return [
            ("Issues Found", result.get("issues_found")),
            ("Status", result.get("label")),
            ("Cleaned KPI Output", result.get("result")),
        ]

    if tool_id == "insights":
        return [
            ("Primary Insight", result.get("primary_insight")),
            ("Executive Implication", result.get("so_what")),
            ("Recommended Action", result.get("recommended_action")),
            ("Suggested Executive Title", result.get("executive_title")),
            ("Suggested Visualization", result.get("chart_suggestion")),
        ]

    if tool_id == "dashboard":
        return [
            ("Executive Summary", result.get("executive_summary")),
            ("Performance Drivers", result.get("performance_drivers")),
            ("Risks & Watch Items", result.get("risks")),
            ("Recommended Action", result.get("recommended_action")),
            ("Outlook", result.get("outlook")),
        ]

    if tool_id == "executive-memo":
        return [
            ("Executive Summary", result.get("summary")),
            ("Background", result.get("background")),
            ("Key Findings", result.get("findings")),
            ("Business Impact", result.get("impact")),
            ("Recommendations", result.get("recommendations")),
            ("Next Steps", result.get("next_steps")),
        ]

    if tool_id == "kpi-health":
        return [
            (
                "Overall Health Score",
                f"{result.get('overall_score', '—')}/100"
            ),
            (
                "Executive Assessment",
                result.get("summary")
            ),
            (
                "Strengths",
                _bullet_lines(result.get("strengths", []))
            ),
            (
                "Concerns",
                _bullet_lines(result.get("concerns", []))
            ),
            (
                "Recommendations",
                _bullet_lines(result.get("recommendations", []))
            ),
        ]

    return [
        ("Analysis Result", str(result))
    ]


def _draw_page_frame(canvas, doc):
    canvas.saveState()

    width, height = LETTER

    # Top brand bar
    canvas.setFillColor(NAVY)
    canvas.rect(
        0,
        height - 0.42 * inch,
        width,
        0.42 * inch,
        fill=1,
        stroke=0
    )

    # Accent stripe
    canvas.setFillColor(MAGENTA)
    canvas.rect(
        0,
        height - 0.45 * inch,
        width,
        0.03 * inch,
        fill=1,
        stroke=0
    )

    # Footer divider
    canvas.setStrokeColor(colors.HexColor("#D9E0EB"))
    canvas.setLineWidth(0.5)

    canvas.line(
        0.65 * inch,
        0.48 * inch,
        width - 0.65 * inch,
        0.48 * inch
    )

    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)

    canvas.drawString(
        0.65 * inch,
        0.30 * inch,
        "Moon Onyx Labs • Executive Insight Engine"
    )

    canvas.drawRightString(
        width - 0.65 * inch,
        0.30 * inch,
        f"Page {doc.page}"
    )

    canvas.restoreState()


def build_analysis_pdf(payload):
    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=LETTER,
        rightMargin=0.65 * inch,
        leftMargin=0.65 * inch,
        topMargin=0.78 * inch,
        bottomMargin=0.70 * inch,
        title=payload.title,
        author="Moon Onyx Labs",
    )

    styles = getSampleStyleSheet()

    brand = ParagraphStyle(
        "Brand",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8,
        textColor=TEAL,
        leading=10,
        letterSpacing=1.1,
        spaceAfter=5,
    )

    report_type = ParagraphStyle(
        "ReportType",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8,
        textColor=MAGENTA,
        leading=10,
        letterSpacing=0.8,
        spaceAfter=6,
    )

    title = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        textColor=DARK_TEXT,
        spaceAfter=8,
    )

    subtitle = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontSize=8.5,
        textColor=MUTED,
        leading=12,
    )

    section_kicker = ParagraphStyle(
        "SectionKicker",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.5,
        leading=10,
        textColor=TEAL,
        letterSpacing=0.9,
        spaceAfter=4,
    )

    section_heading = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=14,
        textColor=DARK_TEXT,
        spaceAfter=8,
    )

    body = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.3,
        leading=14.5,
        textColor=DARK_TEXT,
        alignment=TA_LEFT,
    )

    score_body = ParagraphStyle(
        "ScoreBody",
        parent=body,
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=18,
        textColor=NAVY,
    )

    small = ParagraphStyle(
        "Small",
        parent=styles["Normal"],
        fontSize=7.8,
        leading=10,
        textColor=MUTED,
    )

    center_small = ParagraphStyle(
        "CenterSmall",
        parent=small,
        alignment=TA_CENTER,
    )

    story = []

    # =========================
    # REPORT HEADER
    # =========================

    story.append(
        Paragraph(
            "MOON ONYX LABS",
            brand
        )
    )

    story.append(
        Paragraph(
            "EXECUTIVE INTELLIGENCE REPORT",
            report_type
        )
    )

    story.append(
        Paragraph(
            _escape_text(payload.title),
            title
        )
    )

    meta_values = [
        _safe(payload.toolName, ""),
        _safe(payload.status, ""),
        _format_created_at(payload.createdAt),
    ]

    meta_values = [
        value for value in meta_values if value
    ]

    if meta_values:
        meta_table = Table(
            [[
                Paragraph(
                    _escape_text(value),
                    center_small
                )
                for value in meta_values
            ]],
            colWidths=[
                7.0 * inch / len(meta_values)
                for _ in meta_values
            ]
        )

        meta_table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    LIGHT_BG
                ),
                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    BORDER
                ),
                (
                    "INNERGRID",
                    (0, 0),
                    (-1, -1),
                    0.35,
                    BORDER
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    8
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    8
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    8
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    8
                ),
            ])
        )

        story.append(meta_table)

    story.append(Spacer(1, 18))

    # =========================
    # EXECUTIVE RESULT FIRST
    # =========================

    story.append(
        Paragraph(
            "EXECUTIVE ANALYSIS",
            section_kicker
        )
    )

    story.append(
        Paragraph(
            "Analysis Result",
            section_heading
        )
    )

    for heading, value in _result_sections(
        payload.toolId,
        payload.result
    ):
        if value in (None, "", []):
            continue

        heading_text = _escape_text(heading)

        if (
            "score" in heading.lower()
            or "issues found" in heading.lower()
        ):
            value_style = score_body
        else:
            value_style = body

        card_content = [
            Paragraph(
                heading_text.upper(),
                section_kicker
            ),
            Paragraph(
                (
                    str(value)
                    if "<br/>" in str(value)
                    else _html_text(value)
                ),
                value_style
            ),
        ]

        card = Table(
            [[card_content]],
            colWidths=[7.0 * inch]
        )

        card.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    WHITE
                ),
                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    0.55,
                    BORDER
                ),
                (
                    "LINEBEFORE",
                    (0, 0),
                    (0, -1),
                    3,
                    MAGENTA
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    14
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    14
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    12
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    12
                ),
            ])
        )

        story.append(
            KeepTogether([
                card,
                Spacer(1, 10)
            ])
        )

    # =========================
    # ORIGINAL INPUT SECONDARY
    # =========================

    if payload.input:
        story.append(Spacer(1, 10))

        story.append(
            Paragraph(
                "SOURCE MATERIAL",
                section_kicker
            )
        )

        story.append(
            Paragraph(
                "Original Input",
                section_heading
            )
        )

        input_card = Table(
            [[
                Paragraph(
                    _html_text(payload.input),
                    body
                )
            ]],
            colWidths=[7.0 * inch]
        )

        input_card.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    LIGHT_BG
                ),
                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    0.6,
                    TEAL
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    14
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    14
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    12
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    12
                ),
            ])
        )

        story.append(input_card)

    story.append(Spacer(1, 18))

    story.append(
        Paragraph(
            "Prepared by Moon Onyx Labs for executive review and decision support.",
            small
        )
    )

    doc.build(
        story,
        onFirstPage=_draw_page_frame,
        onLaterPages=_draw_page_frame,
    )

    buffer.seek(0)

    return buffer
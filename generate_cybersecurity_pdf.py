#!/usr/bin/env python3
"""Generate a one-page PDF version of the Cybersecurity CV."""

from pathlib import Path

from reportlab.graphics import renderPDF
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

cv_dir = Path("Cybersecurity_CV")
output_file = cv_dir / "Konstantinos_Kanellopoulos_Cybersecurity_CV.pdf"
photo_file = Path("profile-photo.png")

styles = getSampleStyleSheet()

TITLE = ParagraphStyle(
    "Title",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=20,
    leading=22,
    textColor=colors.HexColor("#0b295f"),
    spaceAfter=0,
)
ROLE = ParagraphStyle(
    "Role",
    parent=styles["BodyText"],
    fontName="Helvetica-Bold",
    fontSize=10.6,
    leading=12,
    textColor=colors.HexColor("#1e3a8a"),
)
CONTACT = ParagraphStyle(
    "Contact",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=8.8,
    leading=10.2,
    textColor=colors.HexColor("#334155"),
)
SECTION = ParagraphStyle(
    "Section",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=9.4,
    leading=10.6,
    textColor=colors.HexColor("#0b295f"),
    spaceAfter=3,
    spaceBefore=1,
)
H3 = ParagraphStyle(
    "H3",
    parent=styles["BodyText"],
    fontName="Helvetica-Bold",
    fontSize=8.9,
    leading=10,
    textColor=colors.HexColor("#0f172a"),
)
ORG = ParagraphStyle(
    "Org",
    parent=styles["BodyText"],
    fontName="Helvetica-Bold",
    fontSize=7.7,
    leading=9,
    textColor=colors.HexColor("#1d4c8f"),
)
BODY = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=7.7,
    leading=9.1,
    textColor=colors.HexColor("#334155"),
)
SMALL = ParagraphStyle(
    "Small",
    parent=BODY,
    fontSize=7.2,
    leading=8.4,
)
TAG = ParagraphStyle(
    "Tag",
    parent=BODY,
    fontName="Helvetica-Bold",
    fontSize=7.2,
    leading=8.4,
    textColor=colors.HexColor("#0f3b73"),
)


def p(text, style=BODY):
    return Paragraph(text, style)


def bullets(items, style=BODY):
    return [Paragraph(f"&bull; {item}", style) for item in items]


def section(title):
    return Paragraph(title, SECTION)


def job(title, date_text, org_text, items):
    rows = [[p(title, H3), p(date_text, H3)] , [p(org_text, ORG), ""]]
    rows.extend([[Paragraph(item, BODY), ""] for item in items])
    table = Table(rows, colWidths=[79 * mm, 35 * mm])
    table.setStyle(TableStyle([
        ("SPAN", (0, 1), (1, 1)),
        ("SPAN", (0, 2), (1, 2)),
        ("SPAN", (0, 3), (1, 3)),
        ("SPAN", (0, 4), (1, 4)),
        ("SPAN", (0, 5), (1, 5)),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    return table


summary_text = (
    "Computer Science student and self-directed cybersecurity learner with hands-on experience in IT support, digital infrastructure, and customer-facing technical roles. "
    "Focused on junior SOC work, including alert triage, log analysis, incident handling, threat detection, and basic vulnerability awareness. "
    "Currently building practical defensive security skills through TryHackMe, daily OWASP Top 10 practice, and structured labs in a personal home environment. "
    "Holds Google Cybersecurity and IT Support certifications. Seeking a junior SOC analyst or cybersecurity internship role where I can apply and grow these skills in a professional environment."
)

training_points = [
    "Progressing through TryHackMe defensive security and SOC-relevant learning paths with 15 hands-on labs completed and a publicly visible profile.",
    "Daily practice reviewing logs, identifying suspicious activity, and documenting findings from personal home lab exercises.",
    "Practical experience with alert triage, vulnerability awareness, manual validation, and remediation workflows.",
    "Hands-on lab experience with incident scenarios, endpoint checks, and basic investigation tasks.",
]

it_points = [
    "Provided first-level IT support for routine user requests and basic troubleshooting.",
    "Maintained and updated website content in WordPress based on department requirements.",
    "Supported digital document archiving and cloud file organisation for internal teams.",
    "Gained foundational understanding of infrastructure, system management, and user-impacting issues useful in SOC work.",
]

additional_roles = [
    ("Sales Agent - Telecommunications", "Aug 2025 - Dec 2025", "iCALL (Vodafone Packages)", [
        "Handled high-volume customer communication, service inquiries, and package recommendations.",
        "Resolved objections and followed structured scripts to improve conversion and satisfaction.",
    ]),
    ("Front Desk Agent", "Jun 2023 - Jul 2023", "Finikas Beach Hotel - Pyrgaki, Naxos, Greece", [
        "Managed front-line customer support, bookings, and payment-related requests under time pressure.",
        "Used HotelBrain PMS to maintain accurate booking records and guest information.",
        "Coordinated with housekeeping and operations for fast issue resolution.",
    ]),
]

skills = [
    "Alert triage",
    "Log analysis",
    "Threat detection",
    "Incident response",
    "Vulnerability awareness",
    "OWASP Top 10",
    "Linux fundamentals",
    "Python for security",
]

technical_skills = [
    "Technical troubleshooting",
    "Cloud file organization",
    "WordPress content management",
    "Windows & Linux admin",
    "Customer communication",
    "Cross-team coordination",
]

education = [
    "BSc Computer Science, University of the People (2024 - ongoing)",
    "Associate in Business Administration, University of the People (2024 - ongoing)",
    "EPAS Computer Technician (2020 - 2022)",
    "7th General Lyceum of Patras (2018)",
]

certifications = [
    "Google Cybersecurity Certificate",
    "TryHackMe Cybersecurity 101",
    "Google IT Support",
    "Python Programming Language (ANKA)",
    "Google UX/UI Design",
    "Google Digital Marketing & E-Commerce",
    "Google Data Analytics (ongoing)",
    "UNICERT Windows Office Suite",
]

licenses = [
    "Car (Category B)",
    "125cc Motorcycle (Category A1)",
    "Speedboat",
    "Drone Operator (A1/A2/A3)",
]

contact_links = [
    "Live CV: konkan2000.github.io/CV_Abroad_Project/Cybersecurity_CV/",
    "GitHub: github.com/konkan2000",
    "TryHackMe: tryhackme.com/p/konkan2000",
]


def qr_drawing(url, size_mm=22):
    widget = qr.QrCodeWidget(url)
    bounds = widget.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    drawing = Drawing(size_mm * mm, size_mm * mm, transform=[size_mm * mm / width, 0, 0, size_mm * mm / height, 0, 0])
    drawing.add(widget)
    return drawing


def tag_row(items):
    return Table([[p(item, TAG) for item in items]], colWidths=[None] * len(items))


header_left = [
    p("Konstantinos Kanellopoulos", TITLE),
    p("Junior SOC Analyst | Cybersecurity Analyst", ROLE),
    p("Patras, Greece", CONTACT),
    p("+30 698 415 6574", CONTACT),
    p("kanell.con00@gmail.com", CONTACT),
    p("Greek (Native), English (C1)", CONTACT),
]

photo = Image(str(photo_file), width=33 * mm, height=42 * mm)
photo.hAlign = "RIGHT"
photo._restrictSize(33 * mm, 42 * mm)

qr_box = Table(
    [[qr_drawing("https://konkan2000.github.io/CV_Abroad_Project/Cybersecurity_CV/"), p("<b>Live CV</b><br/>konkan2000.github.io/CV_Abroad_Project/Cybersecurity_CV/", SMALL)]],
    colWidths=[16 * mm, 32 * mm],
)
qr_box.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#c9d6e6")),
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f3f7fc")),
]))

header_right = Table([[photo], [qr_box]], colWidths=[50 * mm])
header_right.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
]))

header = Table([[header_left, header_right]], colWidths=[128 * mm, 48 * mm])
header.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ("LINEBELOW", (0, 0), (-1, 0), 1.6, colors.HexColor("#1e3a8a")),
]))

summary_block = [section("Professional Summary"), p(summary_text, BODY)]

training_block = [
    section("Security Training & Practice"),
    job(
        "SOC Foundations & Defensive Security",
        "Ongoing",
        "TryHackMe - Hands-on Learning Platform",
        training_points,
    ),
    Spacer(1, 1.2 * mm),
    job(
        "Google Cybersecurity Certificate",
        "Completed 2024",
        "Google Career Certificates",
        [
            "Threat detection, incident response, and network security fundamentals.",
            "Linux fundamentals and Python basics for security automation.",
            "Practical knowledge of security tools, log analysis, and defensive security practices.",
        ],
    ),
    Spacer(1, 1.2 * mm),
    job(
        "TryHackMe Cybersecurity 101",
        "Completed 2024",
        "TryHackMe",
        [
            "Foundational cybersecurity concepts, terminology, and core security principles.",
            "Introduction to defensive and offensive security techniques with practical exercises.",
        ],
    ),
]

it_block = [
    section("IT & Technical Experience"),
    job(
        "Content Management & IT Support Assistant",
        "Jun 2021 - Jun 2022",
        "Region of Western Greece",
        it_points,
    ),
    Spacer(1, 1.2 * mm),
    job(
        "Sales Agent - Telecommunications",
        "Aug 2025 - Dec 2025",
        "iCALL (Vodafone Packages)",
        [
            "Handled high-volume customer communication, service inquiries, and package recommendations.",
            "Resolved objections and followed structured scripts to improve conversion and satisfaction.",
        ],
    ),
    Spacer(1, 1.2 * mm),
    job(
        "Front Desk Agent",
        "Jun 2023 - Jul 2023",
        "Finikas Beach Hotel - Pyrgaki, Naxos, Greece",
        [
            "Managed front-line customer support, bookings, and payment-related requests under time pressure.",
            "Used HotelBrain PMS to maintain accurate booking records and guest information.",
            "Coordinated with housekeeping and operations for fast issue resolution.",
        ],
    ),
]

additional_block = [
    section("Additional Experience"),
    job(
        "Receptionist (Afternoon Shift)",
        "Apr 2023 - May 2023",
        "Pantelia Suites - Fira, Santorini, Greece",
        ["Handled customer requests independently during afternoon operations."],
    ),
    Spacer(1, 1.2 * mm),
    job(
        "Ski Technician",
        "2024 - 2025",
        "Tsakiris Ski Rentals - Bansko, Bulgaria",
        ["Provided technical guidance and practical customer support."],
    ),
    Spacer(1, 1.2 * mm),
    job(
        "Food Delivery Driver",
        "Sep 2022 - Apr 2023",
        "Goody's Burger House - Patras, Greece",
        ["Managed delivery timing, route priorities, and customer communication."],
    ),
]

skills_block = [
    section("Skills, Education, Certifications"),
    p("<b>SOC Skills</b>", H3),
    tag_row(skills),
    Spacer(1, 1.2 * mm),
    p("<b>Technical Skills</b>", H3),
    tag_row(technical_skills),
    Spacer(1, 1.2 * mm),
    p("<b>Education</b>", H3),
    p("<br/>".join(education), BODY),
    Spacer(1, 1.2 * mm),
    p("<b>Certifications</b>", H3),
    p("<br/>".join(certifications), BODY),
    Spacer(1, 1.2 * mm),
    p("<b>Licenses</b>", H3),
    p("<br/>".join(licenses), BODY),
    Spacer(1, 1.2 * mm),
    p("<b>Links</b>", H3),
    p("<br/>".join(contact_links), BODY),
]

left_column = summary_block + [Spacer(1, 1.8 * mm)] + training_block + [Spacer(1, 1.8 * mm)] + it_block + [Spacer(1, 1.8 * mm)] + additional_block
right_column = skills_block

columns = Table([[left_column, right_column]], colWidths=[113 * mm, 63 * mm])
columns.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
]))


def draw_page_border(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#d9e2ef"))
    canvas.setLineWidth(0.8)
    canvas.rect(8 * mm, 8 * mm, A4[0] - 16 * mm, A4[1] - 16 * mm, stroke=1, fill=0)
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(output_file),
    pagesize=A4,
    leftMargin=7 * mm,
    rightMargin=7 * mm,
    topMargin=7 * mm,
    bottomMargin=7 * mm,
)

story = [header, Spacer(1, 2.5 * mm), columns]
doc.build(story, onFirstPage=draw_page_border, onLaterPages=draw_page_border)
print(f"PDF created: {output_file}")

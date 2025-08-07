from fpdf import FPDF
import io

def export_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in content.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf_bytes = io.BytesIO()
    pdf.output(pdf_bytes)
    return pdf_bytes.getvalue()

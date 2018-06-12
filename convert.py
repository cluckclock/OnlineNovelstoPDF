from fpdf import FPDF

def preparedText(text):
    return text.replace('\u2013', '-').replace('\u2014', '-').replace('\u201c', '-').encode('latin-1', 'ignore').decode('utf-8')


class Converter:
    pdf = FPDF()
    def __init__(self):
        self.pdf.add_page()
        self.pdf.set_font('Arial', '', 12)

    def addText(self, text):
        self.pdf.multi_cell(0, 5, preparedText(text))

    def printPDF(self, title):
        self.pdf.output("pdf/" + title + '.pdf', 'F')

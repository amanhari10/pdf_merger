#first run pip install pypdf in your terminal

import pypdf

merger = pypdf.PdfWriter()

for pdf in ["1.pdf", "2.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

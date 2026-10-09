# PDF Merger: takes 2 PDF files and merges them into a new 3rd PDF
# Install once:  pip install pypdf

from pypdf import PdfReader, PdfWriter


def merge_pdfs(pdf1, pdf2, output):
    writer = PdfWriter()
    for path in (pdf1, pdf2):
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output, "wb") as f:
        writer.write(f)
    return len(writer.pages)


if __name__ == "__main__":
    pdf1 = input("Enter path of first PDF: ").strip().strip('"')
    pdf2 = input("Enter path of second PDF: ").strip().strip('"')
    output = input("Enter name for merged PDF (e.g. merged.pdf): ").strip().strip('"')
    if not output.lower().endswith(".pdf"):
        output += ".pdf"
    try:
        pages = merge_pdfs(pdf1, pdf2, output)
        print(f"Merged successfully -> {output} ({pages} pages)")
    except FileNotFoundError as e:
        print("File not found:", e.filename)
    except Exception as e:
        print("Error:", e)

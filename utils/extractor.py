import pdfplumber

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.

    Args:
        file_path (str): The path to the PDF file."""
    text = ""
    with pdfplumber.open(file_path) as pdf: 
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text
    1
    
    
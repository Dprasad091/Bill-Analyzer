import pdfplumber

def extract_data(path):
    with pdfplumber.open(path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    # Simple extraction demo
    # You can use regex to pull units, amount, dates etc.
    data = {
        "units": 345,  # hardcoded or parsed value
        "amount": 1350,
        "month": "May 2025"
    }
    return data

def classify_document(document_text):
    if "car insurance" in document_text.lower():
        return "Car Insurance"
    elif "home insurance" in document_text.lower():
        return "Home Insurance"
    elif "health insurance" in document_text.lower():
        return "Health Insurance"
    else:
        return "Unknown Insurance Type"

from document_processing import load_and_split_document
from document_classification import classify_document
from information_extraction import extract_entities

def run_application(file_path):
    # Step 1: Load and split the document
    document_text = load_and_split_document(file_path)
    # Step 2: Classify the document type
    doc_type = classify_document(document_text)
    print(f"Document Type: {doc_type}")
    # Step 3: Extract information based on document type
    extracted_info = extract_entities(document_text, doc_type)
    print(f"Extracted Info: {extracted_info}")

if __name__ == "__main__":
    file_path = "file:///C:/Users/Vikas/Desktop/Health%20Insurance.pdf"  # Change to your file path
    run_application(file_path)


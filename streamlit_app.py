import streamlit as st
from document_processing import load_and_split_document
from document_classification import classify_document
from information_extraction import extract_entities

# Title of the App
st.title("Insurance Document Analyzer")

# Upload the insurance document
uploaded_file = st.file_uploader("Upload your insurance document", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    # Save the uploaded file temporarily for processing
    with open("temp_doc.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Step 1: Load and split the document
    document_text = load_and_split_document("temp_doc.pdf")
    # Display the raw document content (Optional)
    st.subheader("Raw Document Content:")
    st.write(document_text)

    # Step 2: Classify the document type
    doc_type = classify_document(document_text)
    st.subheader(f"Document Type: {doc_type}")

    # Step 3: Extract relevant information
    extracted_info = extract_entities(document_text, doc_type)
    st.subheader("Extracted Information:")
    for key, value in extracted_info.items():
        st.write(f"{key}: {value}")

else:
    st.write("Please upload a document to analyze.")


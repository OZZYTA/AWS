import boto3
import time

def extract_text_from_pdf(file_path):
    # Initialize Textract client
    textract = boto3.client('textract')

    # Read the PDF file
    with open(file_path, 'rb') as document:
        imageBytes = document.read()

    # Call Textract to extract text
    response = textract.detect_document_text(Document={'Bytes': imageBytes})

    # Extract and print the text
    extracted_text = ""
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            extracted_text += item["Text"] + "\n"

    return extracted_text

if __name__ == "__main__":
    file_path = 'prueba.pdf'
    text = extract_text_from_pdf(file_path)
    print(text)
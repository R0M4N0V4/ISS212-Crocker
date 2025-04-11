'''
Jmoody
Commented by: Emmylee Crocker
ISS 212
4.2025 Wk 12 Tool Development 8 - whatthepdf1.py
Citation: Python for Networking & Security vol 3 - JOrtega
'''

# Import the PDF reader class from PyPDF2 to access PDF content and metadata
from PyPDF2 import PdfReader

# Import os to check file paths
import os

# Define a function to get and print metadata from a PDF file
def get_metadata():
    # Prompt user to enter the full path to the PDF file
    pdf_path = input("Enter the path to the PDF file: ")

    # Check if the file exists on the system
    if not os.path.isfile(pdf_path):
        print("Invalid file path. Please make sure the file exists.")
        return  # Stop execution if the file doesn't exist

    # Print the start of the metadata output
    print("[--- Metadata : " + pdf_path)
    print("------------------------------------------------------------------------------------")

    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfReader object to parse the PDF
        pdfReader = PdfReader(pdf_file)

        # Access the document's metadata (author, title, etc.)
        info = pdfReader.metadata

        # Loop through each metadata item and print it in a readable format
        for metaItem in info:
            print('[+] ' + metaItem.strip('/') + ': ' + info[metaItem])

        # Print the page layout setting (if available)
        layout = pdfReader.page_layout
        print('[+] Layout: ' + str(layout))

        # Access embedded XMP metadata from the PDF
        xmpinfo = pdfReader.xmp_metadata

        # Check and print selected fields from the XMP metadata if they exist
        if hasattr(xmpinfo, 'dc_contributor'): print('[+] Contributor:', xmpinfo.dc_contributor)
        if hasattr(xmpinfo, 'dc_identifier'): print('[+] Identifier:', xmpinfo.dc_identifier)
        if hasattr(xmpinfo, 'dc_date'): print('[+] Date:', xmpinfo.dc_date)
        if hasattr(xmpinfo, 'dc_source'): print('[+] Source:', xmpinfo.dc_source)
        if hasattr(xmpinfo, 'dc_subject'): print('[+] Subject:', xmpinfo.dc_subject)
        if hasattr(xmpinfo, 'xmp_modify_date'): print('[+] ModifyDate:', xmpinfo.xmp_modify_date)
        if hasattr(xmpinfo, 'xmp_metadata_date'): print('[+] MetadataDate:', xmpinfo.xmp_metadata_date)
        if hasattr(xmpinfo, 'xmpmm_document_id'): print('[+] DocumentId:', xmpinfo.xmpmm_document_id)
        if hasattr(xmpinfo, 'xmpmm_instance_id'): print('[+] InstanceId:', xmpinfo.xmpmm_instance_id)
        if hasattr(xmpinfo, 'pdf_keywords'): print('[+] PDF-Keywords:', xmpinfo.pdf_keywords)
        if hasattr(xmpinfo, 'pdf_pdfversion'): print('[+] PDF-Version:', xmpinfo.pdf_pdfversion)

# Ensure the script runs the function only if it's the main program
if __name__ == "__main__":
    get_metadata()

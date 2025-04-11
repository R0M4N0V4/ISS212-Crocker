'''
Jmoody
Commented By: Emmylee Crocker
ISS 212
4.2025 Wk 12 Tool Development 8 - whatthepdf2.py
Citation: Python for Networking & Security vol 3 - JOrtega
'''

# Import the PyPDF2 library to read PDF files
import PyPDF2

# Ask the user to enter the name or full path of the PDF file
pdf_file_name = input("Enter the PDF file name or path: ")

# Try to open the file in binary read mode
try:
    pdfFile = open(pdf_file_name, "rb")
except FileNotFoundError:
    # If the file is not found, print an error message and exit
    print("File not found. Please check the file path.")
    exit(1)

# Create a PdfReader object to read the contents of the PDF
pdfReader = PyPDF2.PdfReader(pdfFile)

# Ask the user for the page number they want to extract text from
page_number = input("Enter page number: ")

# Convert the user input from string to integer
page_number = int(page_number)

# Check if the page number is valid for the given PDF
if page_number < 1 or page_number > len(pdfReader.pages):
    print("Invalid page number. Please enter a valid page number.")
    exit(1)

# Get the page object for the specified page (adjusted to 0-based index)
pageObj = pdfReader.pages[page_number - 1]

# Extract the text from that page
text_pdf = pageObj.extract_text()

# Print the extracted text to the console
print(text_pdf)

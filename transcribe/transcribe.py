import fitz
import pytesseract
import cv2
import numpy as np

# Path to the PDF file
pdf_path = 'transcribe/report.pdf'

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function for image preprocessing
def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Denoise using a bilateral filter
    denoised = cv2.bilateralFilter(gray, 9, 75, 75)

    # Apply adaptive thresholding
    threshold = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

    # Invert the thresholded image
    inverted = cv2.bitwise_not(threshold)

    return inverted

# Function for OCR using Tesseract
def perform_ocr(image):
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')

    return text

# Load the PDF
document = fitz.open(pdf_path)

# Load page 2
page = document.load_page(1)  # Assuming pages are zero-indexed

# Get the image on the page
images = page.get_images(full=True)

# Extract text from the image(s)
extracted_text = ''
for img_index, img in enumerate(images, start=1):
    xref = img[0]
    base_image = document.extract_image(xref)
    image_bytes = base_image["image"]
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)

    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Perform OCR on preprocessed image
    text = perform_ocr(preprocessed_image)

    # Append the extracted text to the result
    extracted_text += f"Extracted Text from Image {img_index}:\n{text}\n\n"

# Print the extracted text
print(extracted_text)

# Close the PDF
document.close()


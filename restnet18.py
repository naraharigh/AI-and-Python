

import sys
import subprocess
import fitz  # PyMuPDF for PDF to image conversion
from PIL import Image
import cv2
import numpy as np
import torch
import torchvision.models as models
import torchvision.transforms as transforms
import torch.nn as nn
# 1. Convert PDF to Imagesquit
def pdf_page_to_image(pdf_path, page_number):
    """Converts a specific page of a PDF into a PIL Image object."""
    doc = fitz.open('C:\work\Python-Algorithms-main\pdf\linux_commands.pdf')
    page = doc[page_number - 1]
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return img

# 2. Image Preprocessing for ResNet-18
def preprocess_image_for_resnet(image, target_size=(224, 224)):
    """Applies preprocessing for a ResNet-18 model (resize, normalize)."""
    transform = transforms.Compose([
        transforms.Resize(target_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) # ImageNet normalization
    ])
    return transform(image).unsqueeze(0) # Add batch dimension

# 3. Text Detection (Placeholder)
def detect_text_regions(image):
    """
    Conceptual: In a full OCR system, you'd use a text detection model
    (e.g., EAST, CRAFT) to identify bounding boxes of text regions.
    For simplicity, the entire image contains text.
    """
    # This would involve another neural network (e.g., a Faster R-CNN or YOLO based model)
    # trained to identify text bounding boxes.
    # For now, return a single bounding box representing the entire image.
    width, height = image.size
    return [{'box': (0, 0, width, height), 'text_region_image': image}]

# 4. Text Recognition with ResNet-18 (Feature Extractor) and a Sequence Model (Conceptual)
class OCRModel(nn.Module):
    def __init__(self, num_classes):
        super(OCRModel, self).__init__()
        # Load a pre-trained ResNet-18 model as the feature extractor
        self.resnet = models.resnet18(pretrained=True)
        
        # Remove the final classification layer
        self.resnet.fc = nn.Identity()

        # Add a text recognition head (e.g., a Bidirectional LSTM)
        # This part requires significant architectural design and training for OCR
        # The 'num_classes' would be the size of your character set + 1 for blank token
        # This example uses a simplified linear layer for illustration
        num_features = 512 # Output features from ResNet-18's average pooling layer
        self.recognition_head = nn.Linear(num_features, num_classes) # Very simplified

    def forward(self, x):
        features = self.resnet(x)
        output = self.recognition_head(features)
        return output

# --- Main Execution ---
    
def read_main_pdf():
    pdf_file = "C:\work\Python-Algorithms-main\pdf\linux_commands.pdf"  # Replace with your PDF file
    page_number = 1
    
    # 1. Convert PDF page to image
    pil_image = pdf_page_to_image(pdf_file, page_number)

    # 2. Preprocess the image for ResNet-18
    processed_image = preprocess_image_for_resnet(pil_image)

    # 3. Text Detection (using a placeholder for now)
    text_regions = detect_text_regions(pil_image) # Use original PIL image for detection

    extracted_text = []

    # 4. Iterate through detected text regions and perform recognition
    for region in text_regions:
        text_region_image = region['text_region_image']

        # Preprocess the text region image for ResNet
        processed_text_region = preprocess_image_for_resnet(text_region_image)

        # Initialize and load your trained ResNet-based OCR model
        # You would replace this with loading your actual trained model weights.
        # For demonstration purposes, we'll create a dummy model and assume character classes.
        # In a real OCR system, num_classes would be based on your character set (e.g., A-Z, a-z, 0-9, etc.)
        
        # Define the number of output classes (e.g., characters + a blank token)
        num_classes = 80 # Example: ASCII characters + special chars + blank
        
        ocr_model = OCRModel(num_classes=num_classes)
        # Assuming you have a pre-trained model checkpoint:
        # ocr_model.load_state_dict(torch.load("your_trained_resnet_ocr_model.pth"))
        ocr_model.eval() # Set to evaluation mode

        # Perform inference
        with torch.no_grad():
            output = ocr_model(processed_text_region)
            # The 'output' will be raw logits or probabilities for each character class.
            # You'll need to decode this output into actual text using techniques like CTC (Connectionist Temporal Classification).
            
            # --- Simplified Decoding (for illustration, not a real OCR output) ---
            # For demonstration, pick the argmax as if it were characters,
            # but this is **not** how a real sequence model works.
            _, predicted_indices = torch.max(output, 1)
            
            # Assuming you have a mapping from indices to characters
            char_map = "management commands" # Example
            decoded_text = "".join([char_map[idx] for idx in predicted_indices.squeeze().tolist()])
            # --------------------------------------------------------------------

            extracted_text.append(f"Text from region at {region['box']}: {decoded_text}")

    # Print the extracted text
    for text in extracted_text:
        print(text)
def install_package(package_name):
    """Installs a Python package using pip as a subprocess."""
    try:
        print(sys.executable)
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")

if __name__ == "__main__":
    package_to_install = "numpy"  # Replace with the desired package name
    install_package(package_to_install)

    package_to_install = "Pillow"  # Replace with the desired package name
    install_package(package_to_install)

    package_to_install = "opencv-python"  # Replace with the desired package name
    install_package(package_to_install)

    package_to_install = "cv2"  # Replace with the desired package name
    install_package(package_to_install)

    package_to_install = "torch"  # Replace with the desired package name
    install_package(package_to_install)

    # torch torchvision torchaudio

    package_to_install = "torchvision"  # Replace with the desired package name
    install_package(package_to_install)

    package_to_install = "PyMuPDF"  # Replace with the desired package name
    install_package(package_to_install)

    read_main_pdf()

import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Function to load image
def load_image(image_path):
    return Image.open(image_path)

# Function to generate description from image
def generate_image_description(image_path):
    # Load the pre-trained BLIP model and processor
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Load and process the image
    image = load_image(image_path)
    inputs = processor(images=image, return_tensors="pt")

    # Generate description using the model
    output = model.generate(**inputs)
    description = processor.decode(output[0], skip_special_tokens=True)

    return description

# Main function
if __name__ == "__main__":
    image_path = "your_image.jpg"  # Replace with your image file path
    description = generate_image_description(image_path)
    print(f"Generated Description: {description}")

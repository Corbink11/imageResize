import os
from PIL import Image
import io

# Configuration
INPUT_FOLDER = "Path\\to\\photos"
OUTPUT_FOLDER = "output\\folder"
MAX_SIZE_KB = 250
MAX_DIMENSION = 3500
QUALITY_DECREMENT = 5  #How much to reduce quality each iteration

def resize_image(image):
    """Resize image so its longest dimension is no more than MAX_DIMENSION."""
    width, height = image.size
    if max(width, height) <= MAX_DIMENSION:
        return image  

    scaling_factor = MAX_DIMENSION / float(max(width, height))
    new_size = (int(width * scaling_factor), int(height * scaling_factor))
    return image.resize(new_size, Image.LANCZOS)

def save_image_under_size_limit(image, output_path):
    """Save the image reducing quality until it's under MAX_SIZE_KB."""
    quality = 95
    while quality > 10:
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", quality=quality, optimize=True)
        size_kb = buffer.tell() / 1024
        if size_kb <= MAX_SIZE_KB:
            with open(output_path, 'wb') as f:
                f.write(buffer.getvalue())
            return True
        quality -= QUALITY_DECREMENT
    print(f"Warning: Could not reduce image to under {MAX_SIZE_KB}KB: {output_path}")
    return False

def process_images():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            input_path = os.path.join(INPUT_FOLDER, filename)
            output_path = os.path.join(OUTPUT_FOLDER, os.path.splitext(filename)[0] + ".jpg")
            try:
                with Image.open(input_path) as img:
                    img = img.convert("RGB")  #Ensure JPEG compatible
                    resized_img = resize_image(img)
                    save_image_under_size_limit(resized_img, output_path)
                    print(f"Processed: {filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    process_images()
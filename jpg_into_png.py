from PIL import Image
import os


def convert_images_to_png(directory):
    """Converts all JPG and JPEG files in a directory to PNG."""
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            filepath = os.path.join(directory, filename)
            try:
                # Open the image in RGB mode (handles most JPG/JPEG formats)
                img = Image.open(filepath).convert("RGB")
                # Create a new filename with .png extension
                new_filename = os.path.splitext(filename)[0] + ".png"
                new_filepath = os.path.join(directory, new_filename)
                # Save the image as PNG with maximum quality
                img.save(new_filepath, quality=100)
                print(f"Converted '{filename}' to '{new_filename}'")
            except Exception as e:
                print(f"Error converting '{filename}': {e}")


# Get the current directory path
current_dir = os.getcwd()

# Convert images in the current directory
convert_images_to_png(current_dir)

print("Finished converting images.")

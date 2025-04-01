import os
import cv2
from concurrent.futures import ThreadPoolExecutor

def scale_image(file_path, output_folder, target_size=(1024, 1024)):
    """Scales a single image to the target size and saves it to the output folder."""
    try:
        img = cv2.imread(file_path)
        if img is not None:
            resized_img = cv2.resize(img, target_size)
            output_path = os.path.join(output_folder, os.path.basename(file_path))
            cv2.imwrite(output_path, resized_img)
            print(f"Resized and saved: {os.path.basename(file_path)}")
        else:
            print(f"Could not read image: {os.path.basename(file_path)}")
    except Exception as e:
        print(f"Error processing {os.path.basename(file_path)}: {e}")

def scale_images_in_folder(input_folder, output_folder, target_size=(1024, 1024), num_threads=10):
    """Scales all images in a folder using multiple threads."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all image files in the input folder
    image_files = [
        os.path.join(input_folder, f)
        for f in os.listdir(input_folder)
        if f.endswith(('.jpg', '.jpeg', '.png', '.bmp'))
    ]

    # Use ThreadPoolExecutor to process images in parallel
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for file_path in image_files:
            executor.submit(scale_image, file_path, output_folder, target_size)

if __name__ == "__main__":
    input_folder = "images"
    output_folder = "images_resized"
    scale_images_in_folder(input_folder, output_folder)
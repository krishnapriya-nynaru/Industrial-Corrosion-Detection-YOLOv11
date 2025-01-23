import os

# Function to rename images in the folder to "corrosiontest_1", "corrosiontest_2", ...
def rename_images_in_folder(image_folder):
    # Ensure the directory exists
    if not os.path.isdir(image_folder):
        print(f"The folder {image_folder} does not exist.")
        return
    
    # Loop through the images in the folder
    count = 1
    for image_name in os.listdir(image_folder):
        # Check if the file is an image (you can add more extensions if needed)
        if image_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            old_path = os.path.join(image_folder, image_name)
            
            # Create a new filename as "corrosiontest_X"
            new_name = f"corrosiontest_{count}{os.path.splitext(image_name)[1]}"
            new_path = os.path.join(image_folder, new_name)
            
            # Rename the image
            os.rename(old_path, new_path)
            print(f"Renamed: {image_name} -> {new_name}")

            count += 1

    print("Renaming completed.")

# Example usage
image_folder = 'test_images'  # Replace with your image folder path
rename_images_in_folder(image_folder)

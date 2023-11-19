import os
import shutil

def copy_files_from_subfolders(source_dir, destination_dir):
    if not os.path.exists(source_dir) or not os.path.exists(destination_dir):
        print("Source or destination directory does not exist.")
        return

    for subfolder in os.listdir(source_dir):
        subfolder_path = os.path.join(source_dir, subfolder)

        if os.path.isdir(subfolder_path):
            for root, _, files in os.walk(subfolder_path):
                for file in files:
                    source_file_path = os.path.join(root, file)
                    destination_file_path = os.path.join(destination_dir, subfolder, os.path.relpath(source_file_path, subfolder_path))

                    # Create the destination directory if it doesn't exist
                    os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)

                    # Copy the file
                    try:
                        shutil.copy(source_file_path, destination_file_path)
                        print(f"Copied: {source_file_path} to {destination_file_path}")
                    except Exception as e:
                        print(f"Error copying: {source_file_path}")
                        print(e)

# Usage
source_directory = '/users/rrodriguez/pictures/etsy/etsy_bajadas'
destination_directory = '/users/rrodriguez/pictures/etsy/todas-juntas'

copy_files_from_subfolders(source_directory, destination_directory)

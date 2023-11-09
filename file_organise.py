import os
import shutil

# Define the directory you want to organize
directory = 'Your/Directory/Path'

# Create folders for each file type if they don't already exist
for filename in os.listdir(directory):
    file_type = filename.split('.')[-1]  # Extract file extension
    folder_path = os.path.join(directory, file_type.upper())  # Create a folder for each file type

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Move files to their respective folders
    if os.path.isfile(os.path.join(directory, filename)):
        shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))

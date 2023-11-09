import shutil
import os
import datetime

# Define the source and destination directories
source_directory = 'Your/Source/Directory'
backup_directory = 'Your/Backup/Directory'

# Generate a timestamp for the backup folder
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
backup_folder = os.path.join(backup_directory, f"backup_{timestamp}")

# Create the backup folder
os.makedirs(backup_folder)

# Copy files from the source directory to the backup directory
for root, dirs, files in os.walk(source_directory):
    for file in files:
        source_path = os.path.join(root, file)
        destination_path = os.path.join(backup_folder, os.path.relpath(source_path, source_directory))
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.copy(source_path, destination_path)

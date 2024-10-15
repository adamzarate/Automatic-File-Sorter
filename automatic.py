import os
import shutil
import time

# Define the main path
path = r'C:\Users\13237\Desktop\Automatic File Sorter'

# Function to create folders if they don't exist
def create_folders():
    folder_names = ['CSV Files', 'Text Files', 'Image Files']
    for folder in folder_names:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Function to sort files into their corresponding folders
def sort_files():
    file_names = os.listdir(path)

    for file in file_names:
        file_path = os.path.join(path, file)

        if file.endswith(".csv") and not os.path.exists(os.path.join(path, 'CSV Files', file)):
            shutil.move(file_path, os.path.join(path, 'CSV Files', file))

        elif file.endswith(".png") and not os.path.exists(os.path.join(path, 'Image Files', file)):
            shutil.move(file_path, os.path.join(path, 'Image Files', file))

        elif file.endswith(".txt") and not os.path.exists(os.path.join(path, 'Text Files', file)):
            shutil.move(file_path, os.path.join(path, 'Text Files', file))

# Infinite loop to run the script every two hours
def run_every_two_hours():
    while True:
        print("Sorting files...")
        create_folders()
        sort_files()
        print("Waiting for the next run...")
        time.sleep(2 * 60 * 60)  # Wait for 2 hours (2 * 60 * 60 seconds)

# Start the script
if __name__ == "__main__":
    run_every_two_hours()

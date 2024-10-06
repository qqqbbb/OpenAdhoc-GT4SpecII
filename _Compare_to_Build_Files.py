import os
import tkinter as tk
from tkinter import filedialog

def get_folder_path():
    """Opens a file dialog to select a folder and returns the selected folder path."""
    root = tk.Tk()
    root.withdraw()  # Hides the small tkinter window
    folder_selected = filedialog.askdirectory()
    return folder_selected

def compare_folders(folder_a, folder_b):
    """Compares two folders and logs differences where files in Folder B are newer."""
    for root_b, _, files_b in os.walk(folder_b):
        for file_b in files_b:
            file_b_path = os.path.join(root_b, file_b)

            # Construct the corresponding file path in Folder A
            relative_path = os.path.relpath(file_b_path, folder_b)
            file_a_path = os.path.join(folder_a, relative_path)

            # Check if file exists in Folder A
            if os.path.exists(file_a_path):
                # Get modification times for both files
                time_a = os.path.getmtime(file_a_path)
                time_b = os.path.getmtime(file_b_path)

                # Log if the file in Folder B is newer
                if time_b > time_a:
                    print(f'File "{relative_path}" is newer in Folder B.')

def main():
    # Get Folder A and Folder B paths from user
    print("Select Folder A")
    folder_a = get_folder_path()

    print("Select Folder B")
    folder_b = get_folder_path()

    if not folder_a or not folder_b:
        print("Both folders must be selected.")
        return

    # Compare the folders and log the results
    compare_folders(folder_a, folder_b)

if __name__ == '__main__':
    main()

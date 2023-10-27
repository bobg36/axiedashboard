import os

def print_folder_structure(folder_path, indent=""):
    # List all items (files and subdirectories) in the given folder
    items = os.listdir(folder_path)
    
    for item in items:
        item_path = os.path.join(folder_path, item)
        
        if os.path.isfile(item_path):
            # Print the file
            print(indent + f"File: {item}")
        elif os.path.isdir(item_path):
            # Print the directory and its contents
            print(indent + f"Folder: {item}")
            print_folder_structure(item_path, indent + "  ")

# Specify the path to the 'data' folder
folder_path = 'data'

# Call the function to print the folder structure
print(f"Folder Structure for '{folder_path}':")
print_folder_structure(folder_path)

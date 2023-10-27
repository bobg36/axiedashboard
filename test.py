import os

def print_folder_structure(folder_path, indent=''):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            print(indent + "Folder: " + item)
            print_folder_structure(item_path, indent + "  ")
        else:
            print(indent + "File: " + item)

if __name__ == "__main__":
    folder_name = 'data'  # Change this to the folder you want to print the structure of
    if os.path.exists(folder_name) and os.path.isdir(folder_name):
        print(f"Folder structure of '{folder_name}':")
        print_folder_structure(folder_name)
    else:
        print(f"The folder '{folder_name}' does not exist.")

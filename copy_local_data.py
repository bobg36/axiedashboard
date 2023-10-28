import shutil
import os
import time

source_folder = r'C:\Users\bobgu\Desktop\record all sales july 2023\walletpy\marketfloor\website_data'
destination_folder = os.path.abspath('data')  # Full path to 'data' folder in the current working directory

if os.path.exists(destination_folder):
    shutil.rmtree(destination_folder)
    print('data folder deleted')
print(source_folder)

shutil.copytree(source_folder, destination_folder)
print(f"Contents of '{source_folder}' have been copied to '{destination_folder}'.")
print('data folder has been updated')
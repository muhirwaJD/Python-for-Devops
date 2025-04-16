#!/usr/bin/env python3

import requests
import os
import shutil
from datetime import datetime

# Set your folder name
folder_name = "jean_muhirwa"
file_name = f"{folder_name}.txt"
file_url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"

# Check if dir exists and delete it
if os.path.exists(folder_name):
    try:
        shutil.rmtree(folder_name)
        print(f"Directory '{folder_name}' has been removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Create a new directory
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Directory: {folder_name} created.")

# Define local file path
local_file_path = os.path.join(folder_name, file_name)

# Download the file
response = requests.get(file_url)
if response.status_code == 200:
    print("File successfully downloaded.")
    with open(local_file_path, "wb") as file:
        file.write(response.content)
    print("File saved successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
    exit()

# Overwrite file content with user input and timestamp
user_input = input("Describe what you have learned so far in a sentence: ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(local_file_path, "w") as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on: {current_time}")
print("File successfully modified.")

#  Display updated content
with open(local_file_path, "r") as file:
    print("\nYou Entered: ", end='')
    print(file.read())


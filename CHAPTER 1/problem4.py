import os

# Specify the directory path
path = '/'  # Replace with your desired path

# Get the list of all files and directories
entries = os.listdir(path)

print(f"Contents of '{path}':")
for entry in entries:
    print(entry)

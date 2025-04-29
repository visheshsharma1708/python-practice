import os

# Get the directory path (current directory in this case)
directory_path ="/Users"

# List all files and directories in the given path
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:", directory_path)
for item in contents:
    print(item)

import os

# Define a sample dictionary
my_dict = {
    "name": "Vishesh",
    "language": "Python",
    "version": "3.10",
    "platform": os.name  # Use os module here
}

# Clear the screen (optional, just to show os module use)
os.system('cls' if os.name == 'nt' else 'clear')

# Print contents of the dictionary
print("Contents of the dictionary:")
for key, value in my_dict.items():
    print(f"{key} : {value}")

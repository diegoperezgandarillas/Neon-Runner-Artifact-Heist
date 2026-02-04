import os

# Define the path to the input file.
# This assumes 'someThing.py' is in the project root,
# and 'IMPORTANT' is a subdirectory within that root.
file_path = os.path.join('IMPORTANT', 'CLASSIFIED')

try:
    # Open the file, read its contents, and ensure it's closed afterward.
    with open(file_path, 'r') as f:
        content = f.read()

    # Convert the entire content to lowercase.
    lowercase_content = content.lower()

    # Open the same file in write mode ('w') to overwrite it.
    with open(file_path, 'w') as f:
        f.write(lowercase_content)

    print(f"Successfully overwrote '{file_path}' with lowercase content.")

except FileNotFoundError:
    print(f"Error: The file at path '{file_path}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

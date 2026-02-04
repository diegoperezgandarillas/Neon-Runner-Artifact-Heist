import os

# Define the path to the input file.
# This assumes 'someThing.py' is in the project root,
# and 'IMPORTANT' is a subdirectory within that root.
file_path = os.path.join('IMPORTANT', 'CLASSIFIED')
s =  'I AM ALFREDO'

d = {}

for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

try:
    # Open the file, read its contents, and ensure it's closed afterward.
    with open(file_path, 'r') as f:
        content = f.read()

    content_list = list(content)
    r = 0
    for i in range(len(s)):
        l = s[i]
        while r < len(content_list) and content_list[r] != l.lower():
            r += 1

        if r < len(content_list):
            if d[l] > 0:
                d[l] -= 1
                content_list[r] = l
            r += 1

    # Join the list back into a string
    modified_content = "".join(content_list)

    with open(file_path, 'w') as f:
        f.write(modified_content)

    print(f"SecretSecret.")

except FileNotFoundError:
    print(f"Error: The file at path '{file_path}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

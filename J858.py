import re

# Open and read the file
with open('filename.txt', 'r') as file:
    text = file.read()

# Replace "Jesus" with "God"
text = text.replace('Jesus', 'God')

# Remove text in "{x:x}" format so you can read it without chapters and verses
text = re.sub(r'\{\d+:\d+\}', '', text)

# Write the updated text back to the file
with open('filename.txt', 'w') as file:
    file.write(text)

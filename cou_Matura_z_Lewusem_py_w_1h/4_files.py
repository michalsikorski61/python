# Initialize an empty list to store lines from the file
lines = []

# Open the file 'file.txt' in read mode with UTF-8 encoding
with open('file.txt', encoding='UTF-8') as f:
    # Iterate over each line in the file
    for line in f:
        # Strip leading/trailing whitespace from the line and append to the list
        lines.append(line.strip())

# Print the list of lines
print(lines)
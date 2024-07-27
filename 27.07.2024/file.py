filename = input("Enter the filename: ")
try:
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    print(f"Number of words in {filename}: {len(words)}")
except FileNotFoundError:
    print(f"File {filename} not found.")

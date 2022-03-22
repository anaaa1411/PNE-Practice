from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "../P0/sequences/U5.txt"  #The two dots indicate the program where to go

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print(file_contents)
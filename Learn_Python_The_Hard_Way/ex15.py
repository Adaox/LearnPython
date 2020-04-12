# Imports argument variables from sys
from sys import argv

# Unpacks command line variables -> script = [0], filename = [1]
script, filename = argv

# assigns txt variable to open file
txt = open(filename)

# prints formatted string
print(f"Here's your file {filename}:")
# prints contents of file saved to txt variable
print(txt.read())
txt.close()
# Prints string
print("Type the filename again:")
# saves user responce to file_again variable
file_again = input("> ")

# assigns txt_again variable to open file
txt_again = open(file_again)

# prints contents of file saved to txt_again
print(txt_again.read())
txt_again.close()

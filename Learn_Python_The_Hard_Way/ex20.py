# import statement
from sys import argv

# unpacking variables from comand line input
script, input_file = argv

# define function -> prints whole file
def print_all(f):
    print(f.read())


# define function -> puts cursor back to 0th position
def rewind(f):
    f.seek(0)


# define function -> prints single line based on argument passed
def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")


# opens file object and assigns to variable
current_file = open(input_file)
# descriptive print statement
print("First let's print the whole file:\n")
# calls print_all function with variable argument
print_all(current_file)

# descriptive print statement
print("Now let's rewind, kind of like a tape.")

# calls rewind function with variable argument
rewind(current_file)

# descriptive print statement
print("Let's print three lines:")

# counter variable assigned (int) followed by a call to print_a_line w/ variable arguments passed
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

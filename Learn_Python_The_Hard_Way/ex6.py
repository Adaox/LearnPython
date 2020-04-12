# fString formating
# Set variable to int
types_of_people = 10
# Set variable to f-string
x = f"There are {types_of_people} types of people."

# Set variables to strings
binary = "binary"
do_not = "don't"
# Set variable to f-string with defined variables (String within string #1 and #2)
y = f"Those who know {binary} and those who {do_not}."

# Prints variable to console
print(x)
print(y)

# Prints f-string with defined variable (String within a string #3 and #4)
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Set variable to boolean
hilarious = False
# Set variable to f-string with undefined variable
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints string variable and sets undefined variable with .format(variable)
print(joke_evaluation.format(hilarious))

# set variable to string
w = "This is the left side of..."
e = "a string with a right side."

# prints string variables with string concatenation
print(w + e)

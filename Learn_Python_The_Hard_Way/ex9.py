# Here's some strange stuff, remember type it exactly.

# Assigns string to variable
days = "Mon Tue Wed Thu Fri Sat Sun"
# \n creates a new line
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# print with two arguments. A string as well as a variable
print("Here are the days", days, sep=": ")
print("Here are the months", months, sep=": ")

# multiline string /n is *not* needed. Whitespace is literal
print(
    """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6.
"""
)

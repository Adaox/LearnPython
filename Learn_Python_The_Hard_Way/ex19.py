# Defines our function with 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


# prints descriptive text followed by calling our function with direct values as arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# prints descriptive text followed by assigning variables, then calling our function with variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints descriptive text followed by calling our function with expressions as arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# prints descriptive text followed by calling our function with expressions as arguments using variables
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # woah! fancy
print(stuff.pop())
print(" ".join(stuff))  # what? cool!
print("#".join(stuff[3:5]))  # super stellar!


# Extra Credit for loop variation
extra_stuff = ["Snack", "Brunch", "Afternoon"]
more_stuff = extra_stuff + more_stuff
print(more_stuff)
for item in range(len(more_stuff)):
    if len(stuff) >= 15:
        break
    else:
        next_item = more_stuff.pop()
        print("Adding: ", next_item)
        stuff.append(next_item)
        print(f"There are {len(stuff)} items now.")

print(f"List is now {len(stuff)}:", stuff)

print(more_stuff)

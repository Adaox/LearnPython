# i = 0
numbers = []


def loop(x, y):
    i = 0
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += y
        print("Numbers now: ", numbers)

        print(f"At the bottom i is {i}")


loop(6, 1)

print("The numbers: ")
for num in numbers:
    print(num)

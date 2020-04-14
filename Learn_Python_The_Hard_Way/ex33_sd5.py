numbers = []


def loop(x, y):
    for i in range(0, x, y):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)

        print(f"At the bottom i is {i}")


loop(6, 1)

print("The numbers: ")
for num in numbers:
    print(num)

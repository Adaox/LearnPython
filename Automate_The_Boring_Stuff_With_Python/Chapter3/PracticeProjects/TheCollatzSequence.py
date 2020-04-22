def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1


num = None

while type(num) != int:
    try:
        num = int(input("Enter a number:\n"))
    except ValueError:
        print("That is  not a number.")
while num != 1:
    num = collatz(num)

import sys

while True:
    print("Type exit to exit.")
    responce = input()
    if responce == "exit":
        sys.exit()
    print("You typed " + responce + ".")

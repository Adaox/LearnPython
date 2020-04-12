from sys import argv

script, filename = argv

print(f"We're going to read {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "r")

print(target.read())

print("And finally, we close it.")
target.close()

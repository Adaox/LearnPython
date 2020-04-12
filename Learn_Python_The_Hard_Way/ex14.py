from sys import argv

script, user_name, user_age = argv
prompt = "*** "

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# Study Drill 3 addition
computer_age = int(input(f"How many years have you had your computer?\n{prompt}"))

print(
    f"""
Alright, so you've said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
Wait you're telling me you were {int(user_age) - computer_age} when you bought that computer?! Wild.
"""
)

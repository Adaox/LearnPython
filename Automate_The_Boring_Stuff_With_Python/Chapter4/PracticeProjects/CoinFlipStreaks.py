import random

hStreak = "111111"
tStreak = "000000"
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    testResult = []
    for i in range(100):
        testResult.append(random.randint(0, 1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    listJoined = "".join(map(str, testResult))
    if hStreak in listJoined or tStreak in listJoined:
        numberOfStreaks += 1
print(f"Chance of streak: {numberOfStreaks / 100}%")

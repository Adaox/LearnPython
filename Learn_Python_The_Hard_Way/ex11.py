# to ensure print doesn't create a new line, end=" " is used
print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# to replicate above functionality, space at end of string
twitch_id = input("What is your twitch.tv Username? ")
fav_game = input("What is your favorite game? ")
fav_streamer = input("Who is your favorite streamer to watch on twitch.tv? ")

print(
    f"So, you're {twitch_id} on twitch.tv, {fav_game} is your favorite game and {fav_streamer} is your favorite streamer to watch."
)

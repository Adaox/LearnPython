name = "Raul E. Vasquez"
age = 36  # not a lie
height = 68  # inches
height_cm = round(height * 2.54, 2)  # converts inches to cm
weight = 165  # lbs
weight_kg = round(weight / 2.205, 2)  # converts lbs to kg
eyes = "Brown"
teeth = "White"
hair = "Black"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall. (Or {height_cm} cm tall.)")
print(f"He's {weight} pounds heavy. (Or {weight_kg} kg heavy.)")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

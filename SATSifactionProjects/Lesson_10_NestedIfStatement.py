# Discuss if statements and how to use them
# if elif and else statements
# create a new menu selection application
import random

ital_fat_food = ['Pasta', 'Pizza', 'a Calzone']
ital_fit_food = ['Pasta Salad', 'Skinny Spaghetti', 'Baked Eggplant']

indian_fat_food = ['Butter Chicken', 'Sweets', 'Chicken Tikka']
indian_fit_food = ['Lentils', 'a Spinach Side', 'Indian Yogurt']

pub_fat_food = ['Fish & Chips', 'a Burger', 'Nachos']
pub_fit_food = ['a Garden Salad', 'a Greek Salad', 'a Ceasar Salad']

message = 'Today we recommend'


def random_food(food_type, feel):
    if feel == 1:
        if food_type == 1:
            print(message, random.choice(ital_fat_food))
        elif food_type == 2:
            print(message, random.choice(indian_fat_food))
        elif food_type == 3:
            print(message, random.choice(pub_fat_food))

    if feel == 2:
        if food_type == 1:
            print(message, random.choice(ital_fit_food))
        elif food_type == 2:
            print(message, random.choice(indian_fit_food))
        elif food_type == 3:
            print(message, random.choice(pub_fit_food))
        else:
            print("I don't know what you'd like to eat")


while True:
    try:
        food_type = int(
            input('What are you in the mood to eat today?\n1 - Italian\n2 - Indian\n3 - Pub Food\n\n>'))
        if food_type in range(1, 4):
            break
    except ValueError:
        print('Please Select 1, 2, or 3')

while True:
    try:
        feel = int(input(
            'What kind of food are you in the mood to eat today?\n1 - I feel like fat food\n2 - I feel like fit food\n\n>'))
        if feel in range(1, 3):
            break
    except ValueError:
        print('Please Select 1 or 2')

random_food(food_type, feel)

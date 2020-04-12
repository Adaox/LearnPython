import random
gotwarriors = ['Jon', 'Dany', 'Sam', 'Jorah', 'Bran', 'Arya', 'Brianne',
               'Theon', 'Sansa', 'Jamie']
killed_night_king = random.choice(gotwarriors)
westeros_pop = 100
your_guess = []
print('Someone has killed the Night King!')
print('Identify the guilty party, or 10 Westeros citizens will die every time you lie!\n')
print(f'One of these suspects did the deed:\n')
print(*gotwarriors, sep=', ')
while True:
    # if population =0 game over
    if westeros_pop == 0:
        print('Sorry Everybody is dead. Game over!')
        break
    your_guess = input('Who did it: ').title()
    # the guess = the character, stop the game because they won...
    # print how many survived
    if your_guess == killed_night_king:
        print(f'You won. There are still {westeros_pop} people alive.')
        break
    # for every wrong guess we want to decrement the population by 10
    else:
        westeros_pop -= 10
        print(f'There are {westeros_pop} people still alive in Westeros')

print('Thanks for Playing!')

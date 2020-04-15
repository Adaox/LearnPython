import random

money = 100
welcome = "Welcome to iC0N Casino! You have " + str(money) + " dollars to spend."
# sg.Popup(welcome)

# Write your game of chance functions here
def cFlip():
    global money

    while True:
        cFlipGuess = input("Please select 'Heads' or 'Tails': ")
        cFlipGuess = cFlipGuess.lower()
        heads = ["heads", "h", "head"]
        tails = ["tails", "t", "tail"]
        hOrT = heads + tails
        if cFlipGuess in heads:
            cFlipGuess = "heads"
        if cFlipGuess in tails:
            cFlipGuess = "tails"
        if cFlipGuess in hOrT:
            break

    while True:
        cFlipBet = input("How much would you like to bet?: ")
        try:
            cFlipBet = int(cFlipBet)
            if 0 < cFlipBet <= money:
                print()
                break
        except ValueError:
            print("Please select a number")

    cFlipResult = random.randint(1, 2)
    if cFlipResult == 1:
        cFlipResult = "heads"
        print("The coin landed on Heads")

    if cFlipResult == 2:
        cFlipResult = "tails"
        print("The coin landed on Tails")

    if cFlipResult == cFlipGuess:
        cFlipWinnings = cFlipBet * 2
        money += cFlipWinnings
        print(
            "You have won, "
            + str(cFlipWinnings)
            + " dollars!! Your new balance is "
            + str(money)
        )
    if cFlipResult != cFlipGuess:
        money -= cFlipBet
        print(
            "You have lost, "
            + str(cFlipBet)
            + " dollars. Your new balance is "
            + str(money)
        )
    return playAgain()


def choHan():
    global money
    while True:
        guess = input("Would you like to guess Odd or Even?: ")
        guess = guess.lower()
        odd = ["odd", "o", "odds"]
        even = ["even", "e", "evens"]
        choHanGuess = odd + even
        if guess in odd:
            guess = "odd"
        if guess in even:
            guess = "even"
        if guess in choHanGuess:
            break

    while True:
        bet = input("How much would you like to bet?: ")
        try:
            bet = int(bet)
            if 0 < bet <= money:
                print()
                break
        except ValueError:
            print("Please select a number")

    diceRoll1 = random.randint(1, 6)
    diceRoll2 = random.randint(1, 6)
    diceTotal = diceRoll1 + diceRoll2
    print(str(diceTotal) + " was rolled")

    if diceTotal % 2 == 0:
        choHanResult = "even"
    if diceTotal % 2 == 1:
        choHanResult = "odd"

    if choHanResult == guess:
        choHanWinnings = bet * 2
        money += choHanWinnings
        print(
            "You have won, "
            + str(choHanWinnings)
            + " dollars! Your new balance is "
            + str(money)
        )
    else:
        money -= bet
        print(
            "You have lost, " + str(bet) + " dollars. Your new balance is " + str(money)
        )
    return playAgain()


def highLow():
    global money

    while True:
        guess = input("Would you like to guess High or Low?: ")
        guess = guess.lower()
        high = ["high", "h"]
        low = ["low", "l"]
        highLowGuess = high + low
        if guess in high:
            guess = "high"
        if guess in low:
            guess = "low"
        if guess in highLowGuess:
            break

    while True:
        bet = input("How much would you like to bet?: ")
        try:
            bet = int(bet)
            if 0 < bet <= money:
                print()
                break
        except ValueError:
            print("Please select a number")

    deckValue = list(range(2, 15)) * 4
    deckSuited = []
    cardValue = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suit1, suit2, suit3, suit4 = " of Spades", " of Hearts", " of Clubs", " of Diamonds"

    for i in cardValue:
        deckSuited.append(i + suit1)
    for i in cardValue:
        deckSuited.append(i + suit2)
    for i in cardValue:
        deckSuited.append(i + suit3)
    for i in cardValue:
        deckSuited.append(i + suit4)
    deckFull = dict(zip(deckSuited, deckValue))
    deck = list(deckFull.keys())
    playerCard = random.choice(deck)
    print("Deck Has been shuffled... \nYou have drawn: " + playerCard)
    deck.remove(playerCard)
    compCard = random.choice(deck)
    print("The Computer has drawn: " + compCard)
    playerCardValue = deckFull[playerCard]
    compCardValue = deckFull[compCard]
    if (playerCardValue > compCardValue and guess == "high") or (
        playerCardValue < compCardValue and guess == "low"
    ):
        highLowWinnings = bet * 2
        money += highLowWinnings
        print(
            "You have won "
            + str(highLowWinnings)
            + " dollars. Your new total is "
            + str(money)
        )
    elif (playerCardValue < compCardValue and guess == "high") or (
        playerCardValue > compCardValue and guess == "low"
    ):
        money -= bet
        print("You have lost " + str(bet) + " dollars. Your new total is " + str(money))
    else:
        print(
            "You and the Computer DRAW! \nNo money gained or lost\nYour total is: "
            + str(money)
        )
    return playAgain()


def roulette():
    global money

    rouletteNumbers = list(range(0, 37))
    rouletteNumbers = map(str, rouletteNumbers)
    rouletteWheel = dict.fromkeys(rouletteNumbers)

    for key in rouletteWheel.keys():
        if (1 <= int(key) <= 10 or 19 <= int(key) <= 28) and (int(key) % 2 == 0):
            rouletteWheel[key] = "black"
        if (1 <= int(key) <= 10 or 19 <= int(key) <= 28) and (int(key) % 2 == 1):
            rouletteWheel[key] = "red"
        if (11 <= int(key) <= 18 or 29 <= int(key) <= 36) and (int(key) % 2 == 0):
            rouletteWheel[key] = "red"
        if (11 <= int(key) <= 18 or 29 <= int(key) <= 36) and (int(key) % 2 == 1):
            rouletteWheel[key] = "black"
    rouletteWheel["0"] = "green"
    rouletteWheel["00"] = "green"

    while True:
        guess = input(
            "Please place your bet: \n(High or Low) \n(Odd or Even)\n(Red, Black, or Green) \n(00-36)\n"
        )
        guess = guess.lower()
        red = ["red", "r"]
        black = ["black", "b"]
        green = ["green", "g"]
        high = ["high", "h"]
        low = ["low", "l"]
        odd = ["odd", "odds", "o"]
        even = ["even", "evens", "e"]
        highLowGuess = high + low
        oddEvenGuess = odd + even
        if guess in high:
            guess = "high"
        if guess in low:
            guess = "low"
        if guess in odd:
            guess = "odd"
        if guess in even:
            guess = "even"
        if guess in red:
            guess = "red"
        if guess in black:
            guess = "black"
        if guess in green:
            guess = "green"
        if guess in highLowGuess or guess in oddEvenGuess:
            break
        if guess in rouletteWheel.values() or guess in rouletteWheel:
            break

    while True:
        bet = input("How much would you like to bet?: ")
        try:
            bet = int(bet)
            if 0 < bet <= money:
                print()
                break
        except ValueError:
            print("Please select a number")

    print("The roulette wheel has been spun, and lands on:")
    rouletteWheelSpin = list(rouletteWheel.keys())
    winningNumber = random.choice(rouletteWheelSpin)
    print(winningNumber + " " + rouletteWheel[winningNumber])

    if winningNumber == guess:
        playerWinnings = bet * 35
        money += playerWinnings
        print(
            "You win big! " + str(playerWinnings) + " Your new total is " + str(money)
        )
    elif guess == rouletteWheel[winningNumber]:
        if guess == "green":
            playerWinnings = bet * 17
        else:
            playerWinnings = bet
        money += playerWinnings
        print(
            "You have won "
            + str(playerWinnings)
            + " dollars. Your new total is "
            + str(money)
        )
    elif guess == "even" and (int(winningNumber) % 2 == 0):
        playerWinnings = bet
        money += playerWinnings
        print(
            "You have won "
            + str(playerWinnings)
            + " dollars. Your new total is "
            + str(money)
        )
    elif guess == "odd" and (int(winningNumber) % 2 == 1):
        playerWinnings = bet
        money += playerWinnings
        print(
            "You have won "
            + str(playerWinnings)
            + " dollars. Your new total is "
            + str(money)
        )
    elif guess == "high" and (int(winningNumber) >= 19):
        playerWinnings = bet
        money += playerWinnings
        print(
            "You have won "
            + str(playerWinnings)
            + " dollars. Your new total is "
            + str(money)
        )
    elif guess == "low" and (int(winningNumber) <= 18):
        playerWinnings = bet
        money += playerWinnings
        print(
            "You have won "
            + str(playerWinnings)
            + " dollars. Your new total is "
            + str(money)
        )
    else:
        money -= bet
        print(
            "You have lost, " + str(bet) + " dollars. Your new balance is " + str(money)
        )
    return playAgain()


def gameChoice():
    while True:
        num = input(
            """Please select a game of chance: 
Coin Flip = 1
Cho Han = 2
High Low = 3
Roulette = 4
"""
        )
        try:
            num = int(num)
            if num in range(1, 5):
                break
        except ValueError:
            print("Hint: Use a number (1-4) to make your selection.")
    if num == 1:
        cFlip()
    elif num == 2:
        choHan()
    elif num == 3:
        highLow()
    elif num == 4:
        roulette()


def playAgain():
    global money
    print()
    if money == 0:
        print(
            "You have no more money, and cannot continue to gamble at iC0N Casino. \nThanks for playing!"
        )
        return
    while True:
        ans = input("Want to play another game? (Y/N)\n")
        ans = ans.lower()
        yes = ["yes", "y"]
        no = ["no", "n"]
        if ans in yes:
            gameChoice()
            break
        elif ans in no:
            print("You are leaving iC0N Casino with " + str(money) + " dollars.")
            print("Thanks for playing!")
            break


# Call your game of chance functions here
print(welcome)
print()
gameChoice()

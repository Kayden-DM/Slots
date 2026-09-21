import random
money = 100

print("Welcome to slots.")


def playagain():
    quit = input("Would you like to quit? (y/n) ").lower().strip()
    if quit == "y":
        print("Thanks for playing.")
    elif quit == "n":
        play()
    else:
        print("Try again. ")
        playagain()


def play():
    global money
    
    if money <= 0:
        print("You have run out of money.")
        exit()

    print(f"You have {money} money.")
    try:
        bet = float(input("Choose a bet amount: "))
    except ValueError:
        print("You must enter a number.")
        play()
        return
    if bet > money:
        print("You don't have enough money.")
        play()
        return
    elif bet <= 0:
        print("You must bet an amount greater than 0.")
        play()
        return
    else:
        print(f"You have bet {bet} money.")
        money -= bet


    number1 = random.randint(0, 10)
    number2 = random.randint(0, 10)
    number3 = random.randint(0, 10)


    print(f"{number1} | {number2} | {number3}")
    if number1 == number2 == number3:
        print("JACKPOT!")
        money += bet * 5
        print(f"You now have {money} money.")
        playagain()
    elif number1 == number2 or number1 == number3 or number2 == number3:
        print("Two right. You have won double your bet.")
        money += bet * 2
        print(f"You now have {money} money.")
        playagain()
    else:
        print("No match. You have lost your bet.")
        playagain()

play()
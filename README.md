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
🎰 Python Slot Machine Game
A simple command-line slot machine game built with Python. Players bet money and spin three random numbers, hoping for a match. It's a great beginner project for learning about functions, global variables, random numbers, and input validation in Python.

📖 Python Slot Machine Game
The Python Slot Machine Game is a console-based gambling simulation. The player starts with 100 money and can place bets on each spin. Three random numbers between 0 and 10 are generated — and depending on how many match, the player either wins a payout or loses their bet.

All three numbers match → Jackpot (5× the bet)

Any two numbers match → Double the bet (2× the bet)

No matches → Lose the bet

The game continues until the player runs out of money or chooses to quit. All bet inputs are validated to ensure they're numbers, positive, and within the player's balance.

This project is ideal for anyone learning the fundamentals of Python — especially functions, loops, and randomization.

✨ Features
Starting balance of 100 money – Gives the player a fixed bankroll to begin with.

Custom bet amounts – The player chooses how much to bet each round.

Three random numbers (0–10) – Generated with random.randint().

Jackpot payout – Three matching numbers pay 5× the bet.

Two-match payout – Any two matching numbers pay 2× the bet.

Loss detection – No matches means the bet is lost.

Bet validation – Rejects non-numeric, negative, zero, or over-budget bets.

Automatic game over – Ends immediately when money reaches zero.

Quit prompt – The player can choose to quit after each spin.

Recursive play loop – The game continues via play() and playagain() functions.

🛠️ What It Uses
Language & Library
Python 3

random – Python's built-in module for generating random numbers.

Key Variables
Variable	Purpose
money	The player's current balance (starts at 100).
bet	The amount the player wagers on a spin.
number1, number2, number3	The three randomly generated numbers.
Key Functions
Function	Purpose
play()	Runs a single round — prompts for a bet, spins the numbers, and checks for wins.
playagain()	Asks the player whether they'd like to quit and handles the response.
Python Concepts Demonstrated
The random module – Using random.randint(0, 10).

The global keyword – Modifying the money variable inside functions.

Functions – Organizing the game into reusable blocks.

Conditional logic – Checking for jackpots, two-match wins, and losses.

Chained comparisons – number1 == number2 == number3 for the jackpot check.

Exception handling – try/except for safe numeric bet input.

Recursion – play() and playagain() call themselves to continue the game.

F-strings – Formatted output for money and bet amounts.

String methods – .lower() and .strip() for clean input.

Built-in Functions Used
input() – Reads user input from the console.

print() – Displays prompts, spins, and results.

float() – Converts the bet input into a decimal number.

random.randint() – Generates a random number between 0 and 10.

exit() – Ends the program when the player runs out of money.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
slots.py
No installation or dependencies are needed — just Python.

▶️ How to Run
Make sure you have Python 3 installed (python.org).

Save the code as slots.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python slots.py
Place your bets and spin to try your luck!

🐍 Made with Python
This project is written entirely in Python 3 using only the standard library. It's a fun and practical example of how functions, conditionals, and randomization can be combined to build a small game.

Whether you're a beginner practicing control flow or someone who enjoys casino-style games, this project is a great starting point.

💡 Possible Future Improvements
Add symbols instead of numbers – e.g., 🍒 🍋 🔔 🍀 to feel more like a real slot machine.

Multiple paylines – Add more reels or diagonal lines for bigger wins.

Adjustable difficulty – Change the number range or payout multipliers.

Add sound effects for wins and losses.

Save and load money between sessions using a file.

Track stats – Wins, losses, biggest payout, and longest streak.

Improve the payout logic – Currently, a two-match win refunds the bet (net zero) because the bet is already deducted. Consider multiplying the payout differently or not deducting the bet first.

Build a Tkinter GUI version for a graphical interface.

📄 License
This project is free to use, modify, and distribute for personal or educational purposes.

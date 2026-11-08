## Slots
A command-line slot machine written in Python. It uses the random module to spin three reels between 0 and 10, and lets the player bet money from a starting balance of 100.

## Features
Three Reels — Spins three random numbers from 0 to 10 on each round.

Jackpot — Pays 5x the bet when all three numbers match.

Two of a Kind — Pays 2x the bet when any two numbers match.

Loss Handling — Loses the bet when no numbers match.

Balance Tracking — Deducts the bet before the spin and adds winnings back to the player's money.

Bet Validation — Rejects non-numeric, non-positive, and oversized bets.

Out of Money — Ends the game when the balance reaches zero.

Play Again — Continues the game or exits based on the user's answer.

## Technologies Used
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `random` | Spins the three reels |
| `random.randint()` | Generates numbers between 0 and 10 |
| `global` | Updates the `money` variable between games |
| `input()` / `print()` | Console interaction |
| `float()` | Parses bet amounts |
| `try / except` | Handles invalid bet input |
| Recursion | Restarts the game via `play()` and `playagain()` |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Save the code as slots.py.

Open a terminal in the folder containing the file.

Run python slots.py.

Enter a bet amount, watch the reels spin, and answer y or n when asked if you want to quit.

## Improvements
Use a loop instead of recursion — play() and playagain() call each other every round, which stacks frames and will eventually hit Python's recursion limit; a while True loop is safer.

Stop the game cleanly on exit — answering y to quit prints "Thanks for playing." but doesn't call exit(), so the player is asked to bet again; call exit() (or sys.exit()) after the message.

Slot Machine
A command-line Python slots game where the player starts with $100 and bets on three random numbers matching.

Concepts Used
Random Module — three random.randint(0, 10) calls simulate the slot reels.

Global Variables — money is updated inside play() using global.

Functions with Recursion — play() and playagain() call each other to keep the game going.

Features
Betting System — the player chooses a bet, deducted before the spin.

Three Payout Tiers — 5x for a jackpot (three of a kind), 2x for any two matching, nothing otherwise.

Balance Tracking — money carries across rounds and the game ends at zero.

Improvements
Validate Bet Input Correctly — a float bet combined with integer payouts causes float drift; also ValueError only catches non-numbers, not negative re-entry loops.

Replace Recursion with a Loop — play() → playagain() → play() stacks calls indefinitely and can crash on long sessions.

Quit Bug — playagain() prints "Thanks for playing" on y but doesn't actually exit; it falls through and restarts.

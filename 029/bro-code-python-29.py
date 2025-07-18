import random

#● ┌ ─ ┐ │ └ ┘

"┌───────────┐"
"│           │"
"│           │"
"│           │"
"└───────────┘"

dice_art ={
    1: ("┌───────────┐"
        "│           │"
        "│     ●     │"
        "│           │"
        "└───────────┘")

    
    (   "┌───────────┐"
        "│   ●       │"
        "│           │"
        "│       ●   │"
        "└───────────┘")
}


dice = []
total = 0
num_of_dice = int(input("how many dice?:"))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total += die
print(f"total: {total}")
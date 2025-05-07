options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
running = True
while running:
    while player not in options:

        player = input("Enter a choice:")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's Tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer == "rock":
        print("you win")
    elif player == "scissors" and computer == "paper":
        print("you win")
    else:
        print("you lose")
        

print("Thanks for the game")
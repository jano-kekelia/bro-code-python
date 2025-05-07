import random

lowest_num = 1
highest_num= 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True


print("python Number Guessing Game")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("enter your guess:")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("that number is out range")
            print(f"please select number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("too low try again")
        elif guess > answer:
            print("Too high try again")
        else:
            print(f"CORRECT The answer was {answer}")
            print(f"Number of guesses {guesses}")
            is_running = False
    else:
        print("invalid guess")
        print(f"please select number between {lowest_num} and {highest_num}")

import random
import math

game_start = "start"

print("Welcome to Game world\n1. Coin flipping\n2. Rolling Die\n3. Number Guessing")
game_option = input("What game do you want to play? ")

if game_option == "coin flipping":
    user_input = input("Type start for coin fliping").lower()
    while user_input == game_start:
        no = random.randint(0, 1)
        if no == 1:
            print("Coin fliped: Head")
        elif no == 0:
            print("Coin fliped: Tail")
        user_input = input("Type start for coin fliping").lower()
        print("dog")

elif game_option == "rolling dice":
    user_input = input("Type start to roll dice").lower()
    while user_input == game_start:
        no = random.randint(1, 6)
        if no == 1:
            print("[-----]\n[-----]\n[  0  ]\n[-----]\n[-----]")
        elif no == 2:
            print("[-----]\n[ 0   ]\n[-----]\n[   0 ]\n[-----]")
        elif no == 3:
            print("[-----]\n[-----]\n[0 0 0]\n[-----]\n[-----]")
        elif no == 4:
            print("[-----]\n[0   0]\n[-----]\n[0   0 ]\n[-----]")
        elif no == 5:
            print("[-----]\n[0    0]\n[  0  ]\n[0    0]\n[-----]")
        elif no == 6:
            print("[-----]\n[0 0 0]\n[     ]\n[0 0 0]\n[-----]")

        print("Welcome to Dice Rolling Simulator")
        user_input = input("Type start to roll dice").lower()

elif game_option == "number guessing":
    lower_range = int(input("Enter the lower range: "))
    higher_range = int(input("Enter the higer range: "))

    random_number = random.randint(lower_range, higher_range)

    print(f"You only have {round(math.log(higher_range - lower_range +1, 2))} chances to guess the integer!")

    count = 0
    while count < math.log(higher_range - lower_range + 1, 2):
        count += 1

        guess_number = int(input("Guess the number"))

        if random_number == guess_number:
            print(f"Congratulation you guess the number in {count} try")
            break
        elif random_number > guess_number:
            print("You guessed too small")
        elif random_number < guess_number:
            print("You guessed too high")

    if count >= math.log(higher_range - lower_range + 1, 2):
        print("\nThe number is %d" % random_number)
        print("\tBetter Luck Next time!")

#!/usr/bin/env python3
## See if your roll hits the monster!

import random

def main():
    ## Intro and game description
    print("Welcome to Attack the Monster!")
    print("You will get 5 chances to hit the monster to defeat it. The monster has 10hp total.")
    print("Each correct guess will damage the monster for 5hp and you gain an extra try.")
    print("Choose wisely")
    print()
    
    ## Create a choice array for user to choose from
    choices = [1, 2, 3, 4, 5, 6, 7, 8]

    ## Generate a random number for monster to take damage
    ## Initialize monster hp and number of tries
    monster_number = random.choice(choices)
    tries = 5
    monster_hp = 10

    ## While monster's hp is greater than 0, run the loop for user to keep trying
    ## If user correctly guesses the monster number, monster takes 5hp damage
    ## else if user has 0 tries left, game is over
    ## else if monster hp is 0, user wins game
    while monster_hp > 0:
        try:
            user_guess = int(input("Choose a number between 1 and 8 to see if you hit the monster!: "))
        
            if user_guess > 8 or user_guess < 1:
                print("Please choose a number between 1 and 8")
                continue

            if user_guess == monster_number:
                monster_hp = monster_hp - 5
                if monster_hp == 0:
                    print("Congrats! You defeated the monster!")
                    break
                print(f"Nice! You hit the monster. It has {monster_hp}hp left.")
                monster_number = random.choice(choices)
                tries = tries + 1
                print(f"You earned an extra try. {tries} tries left")
            elif tries == 0:
                print("Sorry, you used all your tries and lost..")
                break
            else:
                tries = tries - 1
                print(f"Sorry, you didn't hit. You have {tries} tries left.")
        except ValueError as err:
            print("That was not a legal value for division:", err)

    print("Exiting program.")

if __name__ == "__main__":
    main()

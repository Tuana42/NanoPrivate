import random

#kleuren die ik heb gebruikt
pink = "\033[95m"
purple = "\033[35m"
grey= "\033[37m"
reset= "\033[0m"
grey_background = "\033[100m"
pinkt_background = "\033[45m"
RESET = "\033[0m"
yellow= "\033[93m"
green= "\033[92m"
blue= "\033[34m"
red = '\33[91m'

"""Spel regels van het spel"""
def menu_numbergame():
        print("I am so happy to play a game with you!\n")
        input("Press enter for the game rules")
        print("\n                          * Game Rules *")
        print("                              Rule 1:")
        print("        You can make a total of 10 guesses. After every 5 guesses,")
        print("           I will tell you how many guesses you’ve made so far.")
        print("                              Rule 2:")
        print("            I will choose one random number between 1 and 100.")
        print("    You will guess the number, and I'll give you hints when you are closer.")
        print("                            *Good Luck*")
        print("                          \nLet's start!\n")
        numbergame()

"""Hier begint het nummer spel"""
def numbergame():
    play_again = "yes"

    while play_again.lower() == "yes":
        number = random.randint(1, 100)
        previous_guesses = []
        player_won = False

        for attempts in range(1, 11):
            try:
                guess = int(input(f"{purple}Guess a number: "))
            except ValueError:
                print("Invalid answer, please enter a number.")
                continue
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            if guess in previous_guesses:
                print("You already guessed this number, try another one!")
                continue

            previous_guesses.append(guess)

            if guess == number:
                print(
                    f"\n{pink}Congratulations{reset}!\n"
                    f"You guessed the number {number} correctly in {attempts} attempts!\n")
                player_won = True
                break
            elif abs(guess - number) == 1:
                print(f"{reset}You're almost there! Just 1 away!{reset}")
            elif abs(guess - number) <= 2:
                print(f"{pink}You're very close!{reset}")
            elif guess < number:
                print(f"{pink}Guess higher!{reset}")
            else:
                print(f"{purple}Guess lower!{reset}")


            if attempts % 5 == 0:
                print(f"\nYou've made {attempts} guesses so far.\n")

        if not player_won:
            print(f"{red}Sorry{reset}, you didn't guess the number, It was {number}.\n")

        play_again = input(f"Do you want to play again?\nAnswer with {green}yes{reset} or {red}no{reset}: \n")
        if play_again.lower() == "no":
                print(f"\n{pink}Thanks for playing! See you next time{reset}.\n{purple}you are returning to the main menu{reset}")
                break
        elif play_again.lower() == "yes":
            print("I am happy to play again!\n")
            numbergame()

        return numbergame

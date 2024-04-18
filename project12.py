import random
import time
import os
def clear_terminal():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
def difficulty_choser():
    print("""   ___ _           _   _   _                __                 _               
  / __(_)_ __   __| | | |_| |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / _\ | | '_ \ / _` | | __| '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /   | | | | | (_| | | |_| | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\/    |_|_| |_|\__,_|  \__|_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
                                                                              """)
    global secret_number
    global difficulty
    global num_of_attempts
    secret_number = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        num_of_attempts = 10
    elif difficulty == "hard":
        num_of_attempts = 5
    else:
        print("Incorrect input. Try again")
        difficulty_choser()
    game()
def again():
    play_again = input("Do you wanna try again? Y/N: ").lower()
    if play_again == 'y':
        time.sleep(1.5)
        clear_terminal()
        difficulty_choser()
    else:
        print("Nice game. See you!")
def game():
    
    global secret_number
    global difficulty
    global num_of_attempts    
    while num_of_attempts > 0:
        guess = int(input(f"You have {num_of_attempts} attempts remaining to guess a number. \nMake a guess: "))
        if guess > secret_number:
            if num_of_attempts > 1:
                print("Too high.\nGuess again.")
            else:
                print("Sorry, it's too high")
            num_of_attempts -= 1
        elif guess < secret_number:
            if num_of_attempts > 1:
                print("Too low.\nGuess again.")
            else:
                print("Sorry, it's too low.")
            num_of_attempts -= 1
        else:
            print(f"Yes, you are right, the number is {secret_number}.")
            again()
            
    if num_of_attempts == 0:
        print(f"You lost :(\nThe secret number was {secret_number}.")
        again()
        
difficulty_choser()

import random

wanna = 'Y'
while wanna.lower() == "y":
    computer = random.randint(0,2)  
    your = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
    draw = f"Computer chose {computer}. It's a draw!"
    lose = f"Computer chose {computer}. You lose!"
    win = f"Computer chose {computer}. You win!"
    while your != 0 and your != 1 and your != 2:
        your = int(input("Type a valid number (0, 1 or 2) \n"))

    if your == computer:
        print(draw)
    elif your == 0:
        if computer == 1:
            print(lose)
        else:
            print(win)
    elif your == 1:
        if computer == 0:
            print(win)
        else:
            print(lose)
    else:
        if computer == 0:
            print(lose)
        else:
            print(win)
    wanna = input('Wanna try again? (Type "Y" for yes or "N" for no.) \n')
print("Nice player! See you!")
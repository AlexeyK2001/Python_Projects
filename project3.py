print("Welcome to the treasure island! \n Your mission is to find the treasure.")
first = input('Where do you wanna go (Left or Right)? \n')
while first.lower() != "right" and first.lower() != "left":
    first = input("You need to type 'right' or 'left'! \n")
if first.lower() == "right":
    print("Oh no!!! You fell into a snake nest. You died. Game Over :(")
else:
    print("Congrats, you chose the correct turn and evaded the snake nest.\n You are now near the river which you need to cross. ")
    second = input("Would you like to swim or wait for the boat? ('Swim or 'Boat') \n")
    while second.lower() != 'swim' and second.lower() != 'boat':
        second = input("You need to type 'Swim' or 'Boat'! \n")
    if second.lower() == "swim":
        print("Oh shit, you have been eaten by a croco. Game Over :(\n")
    else:
        print("Whew, nice choice, and You are alive!\n Now you finally have come to a temple with the treasure, but it has three doors: Yellow, Blue and Red. \n")
        third = input("Which door will you enter? \n")
        while third.lower() not in ["red", "blue", "yellow"]:
            third = input("You need to type 'red', 'yellow' or 'blue'! \n")
        if third.lower() == "red":
            print('Oh, God. The crazy tiger jumped on you from the door and ate your face. Game Over :( ')
        elif third.lower() == "blue":
            print("Damn, this is a room with the poisoned gas. You breathed it and died! Game Over :( ")
        else:
            print("Lucky you! You passed every challenge unhurt and alive! You can collect your treasure! (It's my semen by the way) ")

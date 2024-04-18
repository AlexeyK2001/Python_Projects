import random
def start_a_game():
    """
    Starts a game of BlackJack
    """
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_cards = [random.choice(card_list), random.choice(card_list)]
    current_score = 0
    computer_score = 0
    play_again = ''
    one_more = True
    current_score = sum(your_cards)
    computer_cards = [random.choice(card_list)]
    if current_score == 21:
        print(f"Your cards: {your_cards}, your current score: {current_score}")
        print(f"Congrats! You got BlackJack! \n Let's see, what is the computer's second card")
        computer_cards.append(random.choice(card_list))
        computer_score = sum(computer_cards)
        if computer_score == 21:
            print("Computer has a BlackJack")
        print(f"Computer's cards are {computer_cards} \n Computer score: {computer_score}")
        if current_score == computer_score:
            print("It's a draw! ")
        else:
            print("You win with a BlackJack")
        play_again = input("Do you want to play again? Y or N: ").lower()
        if play_again == "y":
            start_a_game()
        else:
            print("Nice game, see you! ")

    else:
        print(f" Your cards: {your_cards}, your current score: {current_score} \n Computer's first card: {computer_cards}")
        while one_more == True and current_score <=21:
            pick_a_new = input("Type 'y' to get another card, type 'n' to pass: ")
            if pick_a_new == "y":
                new_card = random.choice(card_list)
                your_cards.append(new_card)
                current_score += new_card
                if 11 in your_cards and current_score > 21:
                    your_cards.remove(11)
                    your_cards.append(1)
                    current_score = sum(your_cards)
                print(f"Your cards: {your_cards}. Your score: {current_score}.")

                if current_score > 21:
                    computer_cards.append(random.choice(card_list))
                    computer_score = sum(computer_cards)
                    if computer_score == 21 and len(computer_cards) == 2:
                        print("Computer has a BlackJack")
                    print(f" Your cards: {your_cards}, your current score: {current_score} \n Computer's cards: {computer_cards}. Computer's score: {computer_score}")
                    one_more = False

            else:
                while computer_score < 17: 
                    computer_cards.append(random.choice(card_list))
                    computer_score = sum(computer_cards)
                    if computer_score == 21 and len(computer_cards) == 2:
                        print("Computer has a BlackJack")
                    if 11 in computer_cards and computer_score > 21:
                        computer_cards.remove(11)
                        computer_cards.append(1) 
                        computer_score = sum(computer_cards)
                print(f"Computer cards: {computer_cards}, \n Computer score: {computer_score}")
                one_more = False
        print(f"Your final score is {current_score}. Computer final score is {computer_score}")
        if current_score <= 21 and current_score > computer_score:
            print("You win!!!!")
        elif current_score <= 21 and current_score == computer_score:                       
            print("It's a draw! \n ")
        elif current_score >21:
            print("Computer wins :( \n ")
        elif current_score <=21 and computer_score > current_score and computer_score <=21:
            print("Computer wins :( \n ")
        elif computer_score > 21:
            print("You win!!!")
    play = input("Do you want to play again? (Y or N) ").lower()
    if play == 'y':
        start_a_game()


                  
play = input("Do you want to play BlackJack? (Y or N) ").lower()
if play == 'y':
    start_a_game()
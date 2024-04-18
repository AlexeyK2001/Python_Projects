#HANGMAN 
import random
def game():
    word_list = ["basketball", "football", "tennis", "swimming", "hiking", "camping", "fishing", "cooking", "baking", "painting", "drawing", "photography", "gardening", "running", "jogging", "cycling", "meditation", "yoga", "dance", "singing", "theater", "cinema", "beach", "mountain", "river", "lake", "ocean", "desert", "forest", "park", "city", "country", "continent", "planet", "galaxy", "star", "moon", "sun", "cloud", "rain", "snow", "wind", "lightning", "thunder", "rainbow", "fire", "ice", "volcano", "earthquake", "tsunami", "tornado", "hurricane", "avalanche", "landslide", "drought", "flood", "pollution", "recycling", "environment","house", "tree", "table", "chair", "computer", "book", "pencil", "paper", "phone", "car", "bicycle", "airplane", "boat", "train", "television", "movie", "music", "guitar", "piano", "drum", "violin", "soccer"]
    word = random.choice(word_list)
    hidden_word = []
    for i in range(len(word)):
        hidden_word.append('_')
    print(f"{''.join(hidden_word)} - The word has {len(hidden_word)} letters.")    
    result = ''
    figure_index = 0
    figures =         [   '''
                ________
                |   |
                |   O
                |
                |
                |
               ---
                ''', 
                '''
                ________
                |   |
                |   O
                |   |
                |
                |
               ---
                ''',
                '''
                ________
                |   |
                |   O
                |  /|
                |
                |
               ---
                ''',
                '''
                ________
                |   |
                |   O
                |  /|\\
                |
                |
               ---
                ''',
                '''
                ________
                |   |
                |   O
                |  /|\\
                |  /
                |
               ---
                ''',
                '''
                ________
                |   |
                |   O
                |  /|\\
                |  / \\
                |
               ---
                '''
            ]

    while result != "win":
        
        guess = input("Guess a letter! ").lower()
        
        if guess not in word:
            print("There is no such letter in the word :(")
            print(figures[figure_index])
            figure_index += 1
            if figure_index == 6:
                print(figures[figure_index-1])
                print(f"You lost! The word was '{word}'. ")
                restart = input("Do you want to play again? (Y or N) ").lower()
                if restart == "y":
                    start()
                else:
                    break
                
        else:
            print(f"Right! There is a {guess} letter in the word! ")
            for i, letter in enumerate(word):
                if letter == guess:
                    hidden_word[i] = guess
            print(''.join(hidden_word))
            if hidden_word.count('_') == 0:
                print("Congratulations!!! You win! \n ")
                restart = input("Do you want to play again? (Y or N) ").lower()
                if restart == "y":
                    start()
                else:
                    break

            
def start():
    print("Welcome to the Hangman! Let's start the game!")
    game()         
start()


        
    

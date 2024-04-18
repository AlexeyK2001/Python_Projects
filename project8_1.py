# #def greet_with_name(name): #(name) is a parameter
#     print(f"Welcome {name}!")
#     print(f"How do you do {name}")
#     print("Isn't the weather nice today?")

# #greet_with_name("Badokka")          #"Badokka" is an argument

# def greet_with(name, location):
#     print(f"Welcome {name}!")
#     print(f"How do you do {name}")
#     print(f"Isn't the weather nice today in {location}?")   

# greet_with("Badokka", "London")    #two positional parameters


# def greet_with(name, location):
#     print(f"Welcome {name}!")
#     print(f"How do you do {name}?")
#     print(f"Isn't the weather nice today in {location}?")   

# greet_with(name = "Badokka", location = "London") #two keyword arguments, so the order doesn't matter now

# CAESAR CYPHER
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(input_text, dir, shift_value):
    result = ''
    if dir == "decode":
        for i in input_text:
            if i in alphabet:
                result += alphabet[26+alphabet.index(i) - shift_value % 26]
            else:
                result += i
    else:
        for i in input_text:
            if i in alphabet:
                result += alphabet[alphabet.index(i) + shift_value % 26]
            else:
                result += i
    print(result)
    again = input("Wanna try again? 'Y' or 'N' \n").lower()
    while again != "y" and again != "n":
        again = input("You should type 'Y' or 'N'! \n").lower()
    if again == "y":
        restart()
    else:
        print("Bye")

def start():    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction != "decode" and direction != "encode":
        print("Incorrect input \n")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(input_text = text, dir = direction, shift_value = shift)

def restart():
    start()

start()
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

def start():
    global direction
    global text
    global shift
    global temp_list
    global result
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction != "decode" and direction != "encode":
        print("Incorrect input")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if direction =="decode":
        start_decode()
    else:
        start_encode()


def decode():
    temp_list = []
    result = ''
    for i in text:
        temp_list.append(alphabet[26+alphabet.index(i) - shift])
    result = ''.join(temp_list)
    print(result)
    again = input("Wanna try again? 'Y' or 'N' ")
    if again == "Y":
        temp_list = []
        result = ''
        start()
    else:
        print("Bye")

def encode():
    temp_list = []
    result = ''
    for i in text:
        temp_list.append(alphabet[alphabet.index(i) + shift])
    result = ''.join(temp_list)
    print(result)
    again = input("Wanna try again? 'Y' or 'N' ")
    if again == "Y":
        temp_list = []
        result = ''
        start()
    else:
        print("Bye")



def start_encode():
    encode()
def start_decode():
    decode()
start()
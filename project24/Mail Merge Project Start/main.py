# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
f = open("./Input/Names/invited_names.txt", "r")
name_list = f.readlines(33)

# making a list of names
for i in range(len(name_list)):
    name_list[i] = name_list[i].strip("\n")

# saving the text of the letter in contents variable
with open("./Input/Letters/starting_letter.txt") as example_text:
    contents = example_text.read()


for name in name_list:
    # replacing [name] with an actual name from the list
    name_changed_text = contents.replace("[name]", name)
    # creating a new file with changed name
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
        new_file = new_letter.write(name_changed_text)

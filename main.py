import random
import string

def main():
    printables = list(string.printable)
    whitespace = list(string.whitespace)

    #Requirements
    pass_length = 12

    #Create a list with allowed characters to use in the generated password.
    allowed_chars = create_list(printables, whitespace)

    print(generate_password(allowed_chars, pass_length))

#Take two lists and remove l2 from l1, so in this case we remove whitespace from printables
def create_list(l1, l2):
    characters = []
    for i in l1:
        if i not in l2:
            characters.append(i)

    return characters

def generate_password(characters, length):
    new_list = []
    password = ""
    #Loop over the allowed letters, numbers and symbols and pick random characters and join them to a string
    for char in characters:
        rand = random.randrange(0, len(characters))
        if len(new_list) < length:
            new_list.append(characters[rand])
    
    password = "".join(new_list)
    
    return password
    


main()
import random
import string

printables = list(string.printable)
whitespace = list(string.whitespace)

#Requirements
min_length = 8

#Take two lists and remove l2 from l1, so in this case we remove whitespace from printables
def create_list(l1, l2):
    characters = []
    for i in l1:
        if i not in l2:
            characters.append(i)

    return characters

def generate_password(characters, min_len):
    new_list = []
    password = ""
    for char in characters:
        rand = random.randrange(0, len(characters))
        if len(new_list) < min_len:
            new_list.append(characters[rand])
    
    password = "".join(new_list)
    
    return password
    

def main():
    #Create a list with allowed characters to use in the generated password.
    allowed_chars = create_list(printables, whitespace)

    print(generate_password(allowed_chars, min_length))

main()
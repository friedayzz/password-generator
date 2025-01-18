import random
import string

printables = list(string.printable)
whitespace = list(string.whitespace)


#Take two lists and remove l2 from l1, so in this case we remove whitespace from printables
def create_list(l1, l2):
    characters = []
    for i in l1:
        if i not in l2:
            characters.append(i)

    return characters

def generate_password(characters):
    for char in characters:
        print(char)



def main():
    #Create a list with allowed characters to use in the generated password.
    allowed_chars = create_list(printables, whitespace)

    generate_password(allowed_chars)

main()
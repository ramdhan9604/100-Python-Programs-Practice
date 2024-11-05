import random
import string 


def generate_password(length,include_digits=True,include_special_characters=True):
    characters = string.ascii_letters
    if include_digits:
        characters+=string.digits
    
    if include_special_characters:
        characters+=string.punctuation
    
    password = "".join(random.choice(characters) for _ in range(length))

    return password


password = generate_password(10)

print("The password: ",password)
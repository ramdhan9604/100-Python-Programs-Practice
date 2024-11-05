import random
import string



a = int(input("Enter the length of the password: "))

def GeneratePassword(n):
    characters= string.ascii_letters+string.digits+string.punctuation
    password = "".join(random.choice(characters) for _ in range(a))
    return password



print(f"The random password of {a} length is: ",GeneratePassword(a))


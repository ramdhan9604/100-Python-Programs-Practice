# import re 

# import string 

# email = input("Enter the email id: ")

# a = "@gmail.com"

# if  email.endswith(a):
#     print("Valid")
# else:
#     print("Invalid")

import re

def is_valid_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

input_email = input("Enter an email address: ")

if is_valid_email(input_email):
    print("Valid email address")
else:
    print("Invalid email address")
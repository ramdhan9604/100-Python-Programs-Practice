# import re
# def is_valid_url(url):
#     regex = re.compile(
#     r'^(?:http|ftp)s?://'
#     r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
#     r'localhost|'
#     r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
#     r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
#     r'(?::\d+)?'
#     r'(?:/?|[/?]\S+)$', re.IGNORECASE)
#     return re.match(regex, url) is not None

# input_url = input("Enter a URL: ")
# if is_valid_url(input_url):
#     print("Valid URL")
# else:
#     print("Invalid URL")

import re

def is_valid_url(url):
    return re.match(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$', url) is not None

input_url = input("Enter a URL: ")
print("Valid URL" if is_valid_url(input_url) else "Invalid URL")
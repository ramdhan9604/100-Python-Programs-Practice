string = input("Enter the string: ")

# s = 'abcdefghijklmnopqrstuvwxyz'
# s = s+ s.upper()

s = set(string)

count=len(s)

# print(s)

# count = 0

# for i in s:
#     if i in string:
#         count=count+1

if count>=26:
    print("Given string is  panagram.")
else:
    print("Not panagram.")
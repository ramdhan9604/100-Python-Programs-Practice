number = str(input("Entere the sequence: "))

if number==number[::-1]:
    print("Given sequence is palindrome.")
else:
    print("Not palindrome.")
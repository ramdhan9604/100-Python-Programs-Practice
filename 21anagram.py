a = input("Enter first sequence: ")
b = input("Enter second sequence: ")


def anagram(a,b):
    return sorted(a)==sorted(b)

if anagram(a,b)==1:
    print("Anagram")
else:
    print("Not Anagram")
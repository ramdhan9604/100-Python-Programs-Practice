
def vowel_count(a):
    count=0
    b = 'aeiouAEIOU'
    for i in a:
        if i in b:
            count=count+1
    return count

a = input("Enter the string: ")
print("The total number of vowels in the given string: ",vowel_count(a))
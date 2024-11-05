with open("simple.txt","w") as file:
    file.write("Hay, How are you?")

with open("simple.txt","r") as file:
    print("Data from file",file.read())
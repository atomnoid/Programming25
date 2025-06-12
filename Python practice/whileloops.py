#while loop execute the code infinityy times

name = input("enter your name: ")

while name == "":
    print("you did not type anything")
    name = input("enter your name: ")
print(f"hello {name}")
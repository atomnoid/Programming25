# Making a program that will check if the charecter is a upper case, lower case, digit or special charecter.

ch = input("Enter the character:")
if ch>"0" and ch<="9":
    print("The given character is a digit")
elif ch == ch.lower():
    print("The given character is a lower case character")
elif ch == ch.upper():
    print("The given character is a upper case character")
else:
    print ("The given character is a special character or mixed character")
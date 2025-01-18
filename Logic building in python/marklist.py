# Marklist program
maths = int(input("Enter your marks in maths: "))
computer_science = int(input("Enter your marks in computer science: "))
physics = int(input("Enter your marks in physics: "))
chemistry = int(input("Enter your marks in chemestry: "))
biology = int(input("Enter your marks in biology: "))

total = maths + computer_science + physics +chemistry + biology
avg = total/5
print("Your total marks is: ", total)
print("Your average marks is: ", avg)

if avg > 35 and avg <= 50:
    print("You have obtained D grade")
elif avg > 50 and avg <= 65:
    print("You have obtained C grade")
elif avg > 65 and avg <= 80:
    print("You have obtained B grade")
elif avg > 80 and avg <= 95:
    print("You have obtained A grade")
elif avg > 95 and avg <= 100:
    print("You have obtained A+ grade")
else:
    print("You have failed in the exam")
#basic structure of for loops in python
for i in range(1, 11, 4,):
    print(i)

#we can iterate strings also for example.

cr_num = "1234-5678-9012"
for x in cr_num:
    print(x)

#we can use "continue" to skip the count and use "break" to stop the iteration

for i in range (1, 30):
    if i==25:
        continue
    else:
        print(i)

#lets write a fizz buzz program

for i in range (1, 101):
    if i%3==0:
        print("fizzbuzz")
    else:
        print(i)


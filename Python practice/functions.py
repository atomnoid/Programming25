#Just goint to practice functions by writing few function codes


def birthday_wish(name, age):
    print(f"happy birthday {name}")
    print(f"you are  {age} years old")
birthday_wish("aayush", 20)
birthday_wish("sourav", 19)
birthday_wish("harsh", 20)

#Practice 2

def car_price(name, price):
    print(f"your car is {name} and the price is {price}")
    return
car_price("m2", "$550k")


#practice 3
#scapitalize

def full_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + ' ' + last
name = full_name("aayush", "sourav")
print(name)

    
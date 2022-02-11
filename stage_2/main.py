import random

arg1 = random.randint(2, 9)
operator = random.choice("+-*")
arg2 = random.randint(2, 9)


if operator == "+":
    result = arg1 + arg2
elif operator == "-":
    result = arg1 - arg2
elif operator == "*":
    result = arg1 * arg2

print((str(arg1) + " " + operator + " " + str(arg2)))


answer = int(input())

if answer == result:
    print("Right!")
else:
    print("Wrong!")
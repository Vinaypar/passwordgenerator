
def addition(a, b):
    c = a + b
    print("Addition of two number is", c)


def subtraction(a, b):
    c = a - b
    print("Subtraction of two number is", c)


def multiplication(a, b):
    c = a * b
    print("Multiplication is", c)


def division(a, b):
    c = a // b
    print("Division of two number is", c)


print("Enter your choice")
print(" For Addition 1")
print(" For Subtraction 2")
print(" For Multiplication 3")
print(" For Division 4")
d = int(input())
val1 = int(input("Enter First Number"))
val2 = int(input("Enter Second Number"))

if 1 == d:
    addition(val1, val2)
elif 2 == d:
    subtraction(val1, val2)
elif 3 == d:
    multiplication(val1, val2)
elif 4 == d:
    division(val1, val2)
else:
    print("something wrong try again")

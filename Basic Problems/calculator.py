def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def int_division(a,b):
    return a//b
def float_division(a,b):
    return a/b
def power_of_number(a,b):
    return a**b
def even_odd(a):
    if a%2==0:
        return 1
    else:
        return 0


print("Menu")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Power of a number")
print("6.Even or Odd")


choice=int(input('Enter choice: '))

#Function : It is like a small robot that can do some specific tasks

def sayHellorobot():
    print("Hello Robot")
sayHellorobot()
sayHellorobot()
print("----------------------------------------------------------------------------------")

def coffeeMachine():
    print("coffeMachine is ready")
    print("coffeeMachine is taking coffee beans")
    print("coffeeMachine is taking water")
    print("coffeeMachine is taking milk")
    print("coffeeMachine is taking sugar")
    print("coffeeMachine is making coffee")
    print("coffeeMachine is ready to serve coffee")
    print("----------------------------------------")
coffeeMachine()
coffeeMachine()
print("-----------------------------------------------------------------------------------")

def say_hello(name):
    print(f"Hello{name}!,How are you?")
say_hello("Aarush")
say_hello("Sam")
print("-----------------------------------------------------------------------------------")

def add(num1,num2):
    print(f"addition of {num1} and {num2} is {num1+num2}")
add(12,45)
add(30,24)
print("-----------------------------------------------------------------------------------")

def sub(num1,num2):
    print(f"subtraction of {num1} and {num2} is {num1-num2}")
sub(45,100)
sub(109,203)
print("-----------------------------------------------------------------------------------")

def multi(num1,num2):
    print(f"multiplication of {num1} and {num2} is {num1*num2}")
multi(65,600)
multi(204,273)
print("-----------------------------------------------------------------------------------")

def div(num1,num2):
    print(f"division of {num1} and {num2} is {num1/num2}")
div(34,10)
div(263,23)
print("-----------------------------------------------------------------------------------")

def power(num1,num2):
    print(f"power of {num1} and {num2} is {num1**num2}")
power(10,2)
power(203,4)
print("-----------------------------------------------------------------------------------")

def mod(num1,num2):
    print(f"power of {num1} and {num2} is {num1%num2}")
mod(10,2)
mod(203,4)
print("-----------------------------------------------------------------------------------")

while True:
    print("Welcome to the calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Finding Power")
    print("6.Finding Remainder")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        add(num1,num2)
    elif choice == 2:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        sub(num1,num2)
    elif choice == 3:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        multi(num1,num2)
    elif choice == 4:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        div(num1,num2)
    elif choice == 5:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        power(num1,num2)
    elif choice == 6:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        mod(num1,num2)
    else:
        print("Invalid Choice, Try Again!")
def add(a,b):
    return a+b

def div(a,b):
    return a/b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

while True:
    print("Choice operation: "
          "\n 1) +"
          "\n 2) -"
          "\n 3) *"
          "\n 4) /")
    operation = input("Choose operation: ")
    number1 = int(input("Input your first number: "))
    number2 = int(input("Input your second number: "))

    if operation == 1 or operation == "+":
        print(add(number1,number2))

    if operation == 2 or operation == "-":
        print(sub(number1,number2))

    if operation == 3 or operation == "*":
        print(mul(number1,number2))

    if operation == 4 or operation == "/":
        print(div(number1,number2))



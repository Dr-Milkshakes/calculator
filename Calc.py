def addition(a, b):
    c = a + b
    return c

def subtraction(a, b):
    c = a - b
    return c
    
def multiplication(a, b):
    c = a * b
    return c

def division(a, b):
    if b != 0:
        c = a/b
        return c
    else:
        return "Error! Division by zero."


# operations = {
#     addition: "+", 
#     subtraction: "-", 
#     multiplication: "*", 
#     division: "/"
# }

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}



# Main program to use the calculator
def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    
    # Get the corresponding function from the disctionary and execute it
    if operation in operations:
        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
    else:
        print("Invalid Operation")
        
calculator()
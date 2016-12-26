# file: factorial_p3_function.py
# Simple example program to calculate the factorial of a number
# that is inputted by user

print("Factorial using Python 3\n")

# returns the factorial of the argument number
def factorial(number):
    product = 1
    for i in range(number):
        product = product * (i + 1)
    return(product)

userInput = eval(input("Enter a non-negative integer for factorial: "))
result = factorial(userInput)
print("Result: ",result) 

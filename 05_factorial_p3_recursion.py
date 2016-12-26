# file: factorial_p3_recursion.py
# Simple example program to calculate the factorial of a number by recursion
# that is inputted by user

print("Factorial using Python 3\n")

# returns the factorial of the argument number
def factorial(number):
    if(number <= 1):
        return 1
    else:
        return number * factorial(number - 1)

userInput = eval(input("Enter a non-negative integer for factorial: "))
result = factorial(userInput)
print("Result: ",result) 
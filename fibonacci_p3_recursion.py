# file: fibonacci_p3_recursion.py
# Simple example program to calculate the fibonacci sequence recursively
# that is inputted by user

print("Fibonacci sequence using Python 3 (recursively)\n")

# returns the number of fibonacci
def fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

userInput = eval(input("Enter a non-negative integer for fibonacci: "))
result = fibonacci(userInput)
print("Fibonacci result: ",result) 
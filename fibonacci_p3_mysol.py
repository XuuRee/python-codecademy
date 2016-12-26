# file: fibonacci_p3_mysol.py
# Simple example program to calculate the fibonacci sequence
# that is inputted by user

print("Fibonacci sequence using Python 3\n")

# returns the fibonacci number
def fibonacci(term):
    if(term == 0):
        return 0
    elif(term == 1):
        return 1
    else:
        iteration = 1
        first = 0
        second = 1
        while(iteration < term):
            third = first + second
            first = second
            second = third
            iteration += 1
        return third

userInput = eval(input("Enter a non-negative integer for fibonacci: "))
result = fibonacci(userInput)
print("Fibonacci result: ",result) 

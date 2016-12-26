# file: fibonacci_p3.py
# Simple example program to calculate the fibonacci sequence
# that is inputted by user

print("Fibonacci sequence using Python 3\n")

# returns the number of fibonacci
def fibonacci(n):
    terms = [0, 1]
    iteration = 2
    while(iteration <= n):
        # sequence is adding and adding another number 
        # until we find our number
        terms.append(terms[iteration - 1] + terms[iteration - 2])
        iteration += 1
    return terms[n]

userInput = eval(input("Enter a non-negative integer for fibonacci: "))
result = fibonacci(userInput)
print("Fibonacci result: ",result) 
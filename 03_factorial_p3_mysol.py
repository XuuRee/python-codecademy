# factorial program using Python (my own solution)

print("Factorial using Python 3 (my own solution)\n")

number = eval(input("Enter a non-negative integer for factorial: "))

factorial = 1

for i in range(1,number + 1): # druha pozice = zadane cislo + jedna
    factorial = factorial * i

print("Result: ",factorial)

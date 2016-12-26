# factorial program using Python 3

print("Factorial using Python 3\n")

number = eval(input("Enter a non-negative integer for factorial\n"))
 
product = 1

for i in range(number):
    product = product * (i + 1)

print(product)
# factorial program using Python 2

print("Factorial using Python 2\n")

number = input("Enter a non-negative integer for factorial\n")
 
product = 1

for i in range(number):
    product = product * (i + 1)

print(product)

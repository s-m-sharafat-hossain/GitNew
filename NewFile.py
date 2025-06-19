def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print("The sum is:", result)
def subtract_numbers(a, b):
    return a - b

result = subtract_numbers(10, 4)
print("The difference is:", result)
def multiply_numbers(a, b):
    return a * b

result = multiply_numbers(4, 7)
print("The product is:", result)
def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

result = divide_numbers(12, 4)
print("The quotient is:", result)
def modulus_numbers(a, b):
    return a % b
result = modulus_numbers(10, 3)
print("The modulus is:", result)
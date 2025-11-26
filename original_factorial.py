def calculate_factorial(number):
    if number == 1:
        return 1
    else:
        return number * calculate_factorial(number - 1)

result = calculate_factorial(5)
print(f"The factorial is: {result}")
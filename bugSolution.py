def my_function(a, b):
    if b == 0:
        return "Division by zero!"  # Or raise a custom exception
    else:
        return a / b

result = my_function(10, 0)
print(result) # Output: Division by zero!
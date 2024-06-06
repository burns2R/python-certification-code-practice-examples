def get_docs(func):
    print(func.__doc__)

def add_numbers(num1, num2):
    """Addition"""
    return num1 + num2

get_docs(add_numbers)
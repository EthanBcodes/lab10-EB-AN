
import math

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return b / a
    except ZeroDivisionError as e:
        print(f"Caught an error: {e}")

def log(a, b):
    try:
        if a <= 0 or a == 1:
            raise ValueError("Base 'a' must be greater than 0 and not equal to 1.")
        if b <= 0:
            raise ValueError("Argument 'b' must be greater than 0.")
        return math.log(b,a)
    except ValueError as e:
        print(f"ValueError: {e}")

def exp(a, b):
    return a ** b

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)

def exponent(a, b):
    return a ** b


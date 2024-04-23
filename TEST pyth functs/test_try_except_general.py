num1 = 10
num2 = "k"

try:
    num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero.")
except TypeError:
    print("No non-numeric characters allowed.")
finally:
    print("---")
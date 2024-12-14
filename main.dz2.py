# завдання2
import math

def calculate_factorial(number):
    if number < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних чисел.")
    return math.factorial(number)

# Приклад використання:
number = 5
factorial = calculate_factorial(number)
print(f"Факторіал числа {number} дорівнює {factorial}")
#завданя1

import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Радіус не може бути від'ємним")
    return math.pi * radius**2

# Приклад використання:
radius = 5
area = calculate_circle_area(radius)
print(f"Площа кола з радіусом {radius} дорівнює {area:.2f}")
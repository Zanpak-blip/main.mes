# завдання3
import math


def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("a не може дорівнювати 0, оскільки це не квадратне рівняння.")

    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        return None


# Приклад використання:
a, b, c = 1, -3, 2
roots = solve_quadratic(a, b, c)

if roots:
    print(f"Корені рівняння: {roots}")
else:
    print("Рівняння не має дійсних коренів.")
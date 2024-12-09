# Функція для обчислення суми перших n членів гармонічного ряду
def harmonic_sum(n):

    if n <= 0:
        raise ValueError("Кількість членів ряду повинна бути натуральним числом.")

    sum_harmonic = sum(1 / i for i in range(1, n + 1))
    return sum_harmonic


# Приклад використання
try:
    n_terms = int(input("Введіть кількість членів ряду (n): "))
    result = harmonic_sum(n_terms)
    print(f"Сума перших {n_terms} членів гармонічного ряду: {result:.6f}")
except ValueError as e:
    print(f"Помилка: {e}")

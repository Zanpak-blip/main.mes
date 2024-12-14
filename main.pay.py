# завдання 4
import math
import matplotlib.pyplot as plt
def simulate_throw(speed, angle, g=9.81):
    angle = math.radians(angle)  # Перетворюємо кут у радіани
    vx = speed * math.cos(angle)  # Горизонтальна швидкість
    vy = speed * math.sin(angle)  # Вертикальна швидкість

    # Час польоту
    t_max = 2 * vy / g
    x_coords = []
    y_coords = []

    # Розраховуємо координати з фіксованим часовим кроком
    t = 0
    while t <= t_max:
        x = vx * t
        y = vy * t - 0.5 * g * t ** 2
        x_coords.append(x)
        y_coords.append(y)
        t += 0.1  # Крок часу

    # Побудова графіка
    plt.plot(x_coords, y_coords)
    plt.title("Траєкторія кидка м'яча")
    plt.xlabel("Відстань (м)")
    plt.ylabel("Висота (м)")
    plt.grid(True)
    plt.show()


# Приклад використання:
simulate_throw(20, 45)  # Початкова швидкість 20 м/с, кут 45 градусів
import math
def vector_angle(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))  # Скалярний добуток
    length_v1 = math.sqrt(sum(a ** 2 for a in v1))  # Довжина першого вектора
    length_v2 = math.sqrt(sum(b ** 2 for b in v2))  # Довжина другого вектора

    if length_v1 == 0 or length_v2 == 0:
        raise ValueError("Вектор не може мати нульову довжину")

    cos_theta = dot_product / (length_v1 * length_v2)  # Косинус кута
    cos_theta = max(min(cos_theta, 1), -1)  # Корекція значення
    angle = math.degrees(math.acos(cos_theta))  # Кут у градусах
    return angle


# Приклад використання:
v1 = [1, 0, 0]
v2 = [0, 1, 0]
print(f"Кут між векторами: {vector_angle(v1, v2):.2f} градусів")
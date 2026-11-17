# Тема: Функции и условные конструкции в Python

# ЗАДАНИЕ 1: Функции и условия
# 1.
def calculate_total(price, tax_percent):
    if price < 0 or tax_percent > 20:
        return 'ошибка'
    result = price * (1 + tax_percent/100)
    return result
# 2.


def get_level(points):
    if points >= 100:
        return "Эксперт"
    if points >= 50:
        return "Продвинутый"
    if points >= 20:
        return "Начинающий"
    else:
        return "Новичок"

# ЗАДАНИЕ 2: Функции с условиями и match/case


def process_status(status):
    match status:
        case "active":
            print("Статус активен")
        case "inactive":
            print("Статус неактивен")
        case "pending":
            print("Статус в ожидании")
        case "blocked":
            print("Статус заблокирован")
        case _:
            print("Неизвестный статус")

# ЗАДАНИЕ 1: Работа со словарями и перебор элементов

student = {
    "имя": "Иван",
    "возраст": 20,
    "курс": 2,
    "город": "Москва"
}
print(student.keys())
print(student.values())
for key, value in student.items():
    print(f"Ключ: {key}, Значение: {value}")
for value in student.values():
    print(value)

# ЗАДАНИЕ 2: Удаление элементов и генератор словарей

prices = {
    "яблоко": 50,
    "банан": 30,
    "апельсин": 40,
    "груша": 35,
    "виноград": 60
}
new_prices = prices.copy()
del prices[("груша")]
my_price = prices.pop("виноград")
my_dict = {key: x * 0.9 for key, x in new_prices.items()}
print(my_dict)

# ЗАДАНИЕ 3: Объединение словарей

student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}

my_student = student1.copy()
student1.update(student2)
print(student1)
student3 = {**my_student, **student2}
print(student1)
print(student2)
print(student3)

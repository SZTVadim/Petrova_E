# ЗАДАНИЕ 1: Добавление элементов в список

fruits = ["яблоко"]
fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1, "виноград")

# ЗАДАНИЕ 2: Удаление элементов из списка

fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
last = fruits.pop()

# ЗАДАНИЕ 3: Поиск элементов в списке

fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits.index("банан"))
print(fruits.count("банан"))

# ЗАДАНИЕ 4: Сортировка и реверс списка

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
numbers.reverse()
print(numbers)

# ЗАДАНИЕ 5

cube = [n ** 3 for n in range(1, 9)]
print(min(cube))
print(max(cube))

# ЗАДАНИЕ 6

numbers = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
new_numbers = [x for x in numbers if x > 10]
print(sum(new_numbers))

# ЗАДАНИЕ 7

cities = ["москва", "санкт-петербург", "казань"]
new_list = [city.capitalize() for city in cities]
print(new_list)


# ЗАДАНИЕ 1: Работа с типами данных

строка = "Привет"
целое_число = 42
число_с_точкой = 3.14
список = [1, 2, 3]

print(type(строка))
print(type(целое_число))
print(type(число_с_точкой))
print(type(список))

# ЗАДАНИЕ 2: Преобразование регистра строк

text = "python PROGRAMMING"
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())

# ЗАДАНИЕ 3: Удаление пробелов

text_2 = "  Hello World  "
print(text_2.strip())
print(text_2.lstrip())
print(text_2.rstrip())

# ЗАДАНИЕ 4: Разделение и объединение строк

text_3 = "яблоко,банан,апельсин,груша"
fruits = text_3.split(",")
print(fruits)
new_text = " | ".join(fruits)
print(new_text)

# ЗАДАНИЕ 5: Замена подстрок

text_4 = "Я изучаю Python. Python - это круто!"
new_text = text_4.replace("Python", "Java")
print(text_4)
print(new_text)

# ЗАДАНИЕ 6: Поиск и подсчет

text_5 = "Python программирование на Python"
print(text_5.find("Python"))
print(text_5.count("Python"))
print(text_5.find("Java"))

# ЗАДАНИЕ 7: Проверка типа символов

print("Hello123".isalnum())  # True
print("12345".isdigit())     # True
print("Hello".isalpha())     # True
print("   ".isspace())       # True

# ЗАДАНИЕ 8: Срезы строк

text_6 = "Python very good"
print(text_6[:3])
print(text_6[-3:])
print(text_6[::2])
reversed_text = text_6[::-1]
print(reversed_text)

# ЗАДАНИЕ 9: Экранирование символов

print("Он сказал: \"Привет\"")
print("Первая строка\nВторая строка")

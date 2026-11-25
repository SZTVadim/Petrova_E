# ЗАДАНИЕ 1: Класс Book (Книга)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        return self.pages > 300


book_1 = Book("Мастер и Маргарита", "Булгаков", 290)
book_2 = Book("Горе от ума", "Грибоедов", 200)
book_3 = Book("Братья Карамазовы", "Достоевский", 650)

print(book_1.get_info())
print(book_1.is_long())
print(book_2.get_info())
print(book_2.is_long())
print(book_3.get_info())
print(book_3.is_long())

# ЗАДАНИЕ 2: Класс BankAccount (Банковский счёт)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        print("Недостаточно средств")
        return False

    def get_balance(self):
        return self.balance


account_1 = BankAccount("Катя", 2000)
account_1.deposit(100)
account_1.withdraw(500)
account_1.withdraw(2000)
print(account_1.get_balance())

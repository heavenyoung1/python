from dataclasses import dataclass
from typing import Optional

class BankAccount:
    def __init__(self, owner: str, balance: int =0):
        self.owner_deposit = owner
        self._balance = balance

    def deposit(self, amount: int):
        print(self._balance)
        self._balance = self._balance + amount
        print(f'Вы пополнили счёт на: {amount}, Ваш баланс {self._balance}.')

    def withdraw(self, amount: int):
        if not isinstance(amount, int) or amount <= 0:
            print(f"Некорректная сумма: {amount}")
            return
        if amount > self._balance:
            print(f"Недостаточно средств. Баланс: {self._balance}")
            return
        else:
            self._balance = self._balance - amount
            print(f"Снято: {amount}. Остаток: {self._balance}")
            return

    @property
    def balance(self):
        return self._balance

    def __repr__(self):
        return f'Account Owner: {self.owner_deposit}, deposit balance = {self._balance}'

acc = BankAccount("Bob", 100)
acc.deposit(20)
acc.withdraw(50)
acc.withdraw(200)
print(acc.balance)  # 70
print(acc)
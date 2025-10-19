# Напиши программу, которая проверяет, больше ли число 10.

# user_input = int(input("Введите любое число: "))
# if user_input >= 10:
#     print("Число больше либо равно 10")
# elif user_input == 0:
#     print("Число равно нулю")
# elif user_input < 0:
#     print("Число отрицательное")
# else:
#     print("Число меньше 10")

# Спроси у пользователя возраст и напиши: «школьник», «студент» или «взрослый».

# age = int(input("Сколько тебе лет?: "))
# if (age > 6) and (age < 18):
#     print("Ты школьник!")
# elif age >= 18 and age < 22:
#     print("Ты студент.")
# elif age >= 22:
#     print("Ты взрослый!")
# else:
#     print("Ты сопля!")

# Напиши игру: компьютер загадывает число 5, а пользователь вводит число. Если угадал — победа, иначе — проигрыш.

# number = int(input("Назови число: "))
# guess = 5
# if number == guess:
#     print("Победа!")
# else:
#     print("Проигрыш!")

# day = input("Какой сегодня день?")
# if day == "Суббота" or day == "Воскресенье":
#     print("Сегодня выходной!")
# else:
#     print("Иди на работу!!")


name = input("Введи имя: ")
password = input("Введи пароль: ")
login = "admin"
pas = "1234"
if not (name == login) or not (password == pas):
    print("Уходи")
else:
    print("Входи!")
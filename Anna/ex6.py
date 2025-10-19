# Выведи числа от 1 до 10 с помощью for.

# for i in range(1, 6):
#     #print("2 x",  i, "=", 2 * i)
#     print(f'2 * {i} = {2 * i}')

# count = 0
# while count < 100:
#     count = count + 1
#     print(f"count {count}")
# print("конец")

# password = ""
# while password != "1234":
#     password = input("Скажи пароль:")
#     if password == "1234":
#         print("Здрасте!")


# while True:
#     команда = input("Введите команду: ")
#     if команда == "выход":
#         break
#     print(f"Вы ввели: {команда}")

stroka = 'AAAbbbCCCdddEEEfffGGGhhh'
print(len(stroka))
print(stroka[6])
print(stroka[1:5])
#print(stroka)

print(stroka.upper())
print(stroka.lower())
print(stroka.capitalize())
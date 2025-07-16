# Рекурсия

# def sum(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total

print(sum([1, 2, 3, 4, 5, 6, 7]))

# Стек вызовов с рекурсией

def fact(x):
    if x == 1:
        return 1
    else:
        print(f' Factorial x = {x}')
        print(f'Значение равно = {x * fact(x - 1)}')
        return x * fact(x - 1)

print(fact(5))

# Коl для функции sum

def sum(list):
    if list == []:
        return 0
    else:
        return list[0] + sum(list[1:])

print(f'Result sum {sum([1, 2, 3, 4, 5, 6])}')

# Код для рекурсивной функции подсчёта количества элементов в списке

def count(list):
    if list == []:
        return 0
    else:
        return 1 + count(list[1:])

print(f'Result count {count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}')


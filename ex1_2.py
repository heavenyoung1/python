l = list(range(10))
print(l)

l[2:5] = [10, 20, 30]
print(l)

del l[5:7]
print(l)

l[5::2] = [30, 7]
print(l)

my_list = [[30, 7]] * 3
print(my_list)

listing = []
for i in range(3):
    listing.append(['_'] * 3)
print((listing))

listcomp = [['_'] * 3 for i in range(3)]
print(listcomp)

listcomp[0][1] = 'X'
print(listcomp)

# тестирование

board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)

board[0][0] = "X"
print(board)

#ВНИМАТЕЛЬНО!! один и тот же список в списке
row1 = ['_'] * 3
board1 = []
for i in range(3):
    board1.append(row1)
board1[0][0] = "X"
print(board1)

# Составное присваивание последовательностей

print(id(listcomp))
listcomp *= 2
print(id(listcomp))
tupling = (1, 2, 3, 4)
print(id(tupling))
tupling *= 2
print(id(tupling))

# t = (1, 2, [30, 40])
# t[2] += [50, 60]
# print(t)

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(f'This sorted function - {sorted(fruits)}')

print(f'This sorted function - {sorted(fruits)}')


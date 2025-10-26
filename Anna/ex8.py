fruits = ["яблоко", "банан", "груша", "слива"]
print(fruits[3])
fruits.append('манго')
print(fruits)
print(fruits[-1])
fruits.append('дыня')
print(fruits)
print(len(fruits))
fruits.insert(2, 'авокадо')
print(fruits)
fruits.remove("авокадо")
print(fruits)
fruits.pop()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

for i in fruits:
    print(f"Фрукт - {i}")

for i in range(len(fruits)):
    print(f'Фрукт {i} = {fruits[i]}')

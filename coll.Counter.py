from collections import Counter

ct = Counter('abracadabra')
print(ct)

ct.update('aaaaaaaaaaaazzz')
print(f'Is ct {ct}')
print(ct.most_common(3))


# ---------------------
import collections

class StrKeyDict(collections.UserDict):

     def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

     def __contains__(self, key):
         return str(key) in self.data

     def __setitem__(self, key, item):
             self.data[str(key)] = item

d = StrKeyDict()
d[1] = "one"      # Ключ 1 преобразуется в "1"
d["2"] = "two"    # Ключ "2" остаётся строкой
print(d[1])       # Выведет "one" (поиск по "1")
print("1" in d)   # True (проверка по "1")
#print(d[3])       # KeyError, так как 3 не найдено и это не строка

#d = {1: 'A'}
#d_proxy = MappingProxyType(d)

d = dict(
    a=10,
    b=20,
    c=30,
    d=40,
    e=50,
)
values = d.values()

print(f'Values = {values}')
print(f'Keys = {d.keys()}')
print(f'Items = {d.items()}')
print(f'List values = {reversed(list(values))}')
print(f'Value[0] = {list(values)[0]}')

set_1 = frozenset(range(10))

d1 = dict(a=1, b=2, c=3)
d2 = {'b': 20, 'c': 30, 'd': 50}
print(d1.keys() & d2.keys())
print(f'Type is {type(d1.keys() & d2.keys())}')
s = {'a', 'e', 'i'}

print(d1.keys() & s)
print(type((d1.keys() & s)))

print(d1.keys() | s)
print(*d1)
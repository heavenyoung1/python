from collections import  ChainMap

d1 = dict(a=10, b=2)
d2= dict(a=5, b=4, c=3)

chain = ChainMap(d1, d2)

print(chain['c'])
chain['c'] = 100
print(f' Is d1 {d1}')
print(f' Is d2 {d2}')
print(f' Is chain {chain}')

import builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))

print(f'Is pylookupc {pylookup}')
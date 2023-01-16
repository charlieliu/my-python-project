'''
Mapping Types — dict
https://docs.python.org/3/library/stdtypes.html#dict
'''

def printAll():
    print('a', type(a), a)
    print('b', type(b), b)
    print('c', type(c), c)
    print('d', type(d), d)
    print('e', type(e), e)
    print('f', type(f), f)
    print('deep',   type(deep),     deep)
    print('shallow',type(shallow),  shallow)
    print('====================')
def printCopy():
    print('a',      type(a),        a)
    print('deep',   type(deep),     deep)
    print('shallow',type(shallow),  shallow)
    print('====================')

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
deep = a.copy() # deep copy
shallow = a     # shallow copy
printAll()
# print('list', list(d))
# print('len', len(d))
# print('key', d['one'])
# for key in d: print('key', type(key), key)
# print('in', 'one' in d)
# print('not in', 'one' not in d)
# print('iter(d)', iter(d))
# print('clear()', d.clear())
# print('d', type(d), d)
# print('====================')
# del a['one']
# printCopy()
# print('get()', a.get('one', 0))
# print('items()', a.items())
# for item in a.items(): print('item', type(item), item)
# print('keys()', a.keys())
# for key in a.keys(): print('key', type(key), key)
# a['one'] = 100
# print('pop()', a.pop('one'))
# print('pop()', a.pop('one', 0))
# printCopy()
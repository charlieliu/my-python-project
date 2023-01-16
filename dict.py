'''
Mapping Types — dict
https://docs.python.org/3/library/stdtypes.html#dict
'''
def printA(title=''):
    print('==========', title, '==========')
    print('a', type(a), a)
def printAll(title=''):
    print('==========', title, '==========')
    print('a', type(a), a)
    print('b', type(b), b)
    print('c', type(c), c)
    print('d', type(d), d)
    print('e', type(e), e)
    print('f', type(f), f)
def printCopy(title=''):
    print('==========', title, '==========')
    print('a',      type(a),        a)
    print('deep',   type(deep),     deep)
    print('shallow',type(shallow),  shallow)
# 建立 Dictionary 的方法
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
printAll('建立 Dictionary 的方法')

# 新增 Dictionary 元素的方法
a['four'] = 4
a = dict(a, five=5)
printA('新增 Dictionary 元素的方法')

# 讀取 Dictionary 元素的方法
print('==========', '讀取 Dictionary 元素的方法', '==========')
print('a[\'one\']:', a['one'])
for key in a: print('key:', type(key), key, ', value:', type(a[key]), a[key])
print('\'one\' in a:', 'one' in a)
print('\'one\' not in a:', 'one' not in a)
print('a.get(\'one\'):', a.get('one', 0))
print('a.get(\'six\'):', a.get('six', 0))

# 修改 Dictionary 元素的方法
a['four'] = 44
a = dict(a, five=55)
printA('修改 Dictionary 元素的方法')

# 複製 Dictionary 元素的方法
a['zero'] = a['four']
a['six'] = int(a['zero'])
printA('複製 Dictionary 元素的方法')

# 複製 Dictionary 的方法
deep = a.copy() # deep copy
shallow = a     # shallow copy
printCopy('複製 Dictionary 的方法')

# 刪除 Dictionary 元素的方法
del a['five']
x = a.pop('four')
printCopy('刪除 Dictionary 元素的方法')
print('x', type(x), x)

# 刪除 Dictionary 所有元素的方法
a.clear()
printCopy('刪除 Dictionary 所有元素的方法')

# 其他方法
print('==========', '其他方法', '==========')
print('list(b)', list(b))
print('len(b)', len(b))
print('iter(b)', iter(b))
print('b.items()', b.items())
for item in b.items(): print('item', type(item), item)
print('keys()', b.keys())
for key in b.keys(): print('key', type(key), key)
print('b.items()', b.values())
for item in b.values(): print('item', type(item), item)


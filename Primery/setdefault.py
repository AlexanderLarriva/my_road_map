# import collections
from collections import defaultdict

# функция конструктор с побочным эффектом
def f():
     print('function f() was called!')
     return [] 
 
d = {}
# чтобы передать как дефолтное значение пустой список, 
# нам придется вызвать функцию f() внутри setdefault
print(d.setdefault('a', f()).append(1))
# # => function f() was called!
# # и снова
print(d.setdefault('a', f()).append(2))
# # => function f() was called!
# # и еще раз, несмотря на то, что ключ существует в словаре!
print(d.setdefault('a', f()).append(3))
# # => function f() was called!
print(d) # {'a': [1, 2, 3]}
 
# в случае defaultdict мы можем передать саму функцию
dd = defaultdict(f)
# если ключа нет, то функция будет вызвана
print(dd)
dd['a'].append(1)
print(dd)
# => function f() was called!
# а если ключ есть, то defaultdict получит его значение
dd['a'].append(2)
dd['a'].append(3)
print(dd)
dd # defaultdict(<function __main__.f()>, {'a': [1, 2, 3]})

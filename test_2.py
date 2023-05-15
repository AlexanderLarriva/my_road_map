# def asd(text):
#   result = ''
#   for char in text[::-1]:
#     result += char
#   return result


# print(asd("Privet"))


# def wqe(items):
#    MyDict = {}
#    NewMyDict = {}
#    for item in items:
#      NewMyDict = {True: item}
#      MyDict.update(NewMyDict)
#    return MyDict
   
   
# items = (1, 2, 3, 4)

# print(wqe(items))

# value = "a"

# if ord(value.upper()) in range(65, 91):
#   print("1")

# list(filter(None, ['', 1, 2, 'foo', None, False]))

# def decorator(func):
#     def wrapper():
#         print('функция-оболочка')
#         func()
#     return wrapper

# def basic():
#     print('основная функция')

# wrapped = decorator(basic)
# print('старт программы')
# basic()
# wrapped()
# print('конец программы')

# def decorator(func):
#     '''Основная функция'''
#     print('декоратор')
#     def wrapper():
#         print('-- до функции', func.__name__)
#         func()
#         print('-- после функции', func.__name__)
#     return wrapper

# @decorator
# def wrapped():
#     print('--- обернутая функция')

# print('- старт программы...')
# wrapped()
# print('- конец программы')

# def decorator_1(func):
#     print('декоратор 1')
    
#     def wrapper():
#         print('перед функцией')
#         func()
#     return wrapper

# def decorator_2(func):
#     print('декоратор 2')
    
#     def wrapper():
#         print('перед функцией')
#         func()
#     return wrapper

# @decorator_1
# @decorator_2
# def basic_1():
#     print('basic_1')

# @decorator_1
# def basic_2():
#     print('basic_2')

# print('>> старт')
# basic_1()
# basic_2()
# print('>> конец')
# import collections

# d = collections.OrderedDict()

# # dict = {}

# for i in range(1,6):
#     d[i] = i

# b = dict(d) 
# print(b)

# bank = list(b.items())

# print(bank)
# print(len(bank))


# def factorial(n):
#     print(f'n = {n}')
#     if n <= 0:
#         return 1
#     l = n * factorial(n - 1)
#     print(l)
#     return l

# n = 5
# print(f'factorial of {n} = {factorial(n)}')


# def greetings(st):
#      print(st)
#      if len(st) == 0:  # Граничный случай
#          return             
#      else:       # Рекурсивный случай
#          greetings(st[:-1])   

# greetings('Hello, world!')


# def palindrome(my_str):
#     if len(my_str) == 0 or len(my_str) == 1: # граничный случай
#         return True
#     else: # рекурсивный случай
#         head = my_str[0]
#         middle = my_str[1:-1]
#         end = my_str[-1]
#         return head == end and palindrome(middle)

# st = [i.lower() for i in input() if i.isalpha()]
# print((palindrome(st)))


# def binary_search(items, value):
#     left = 0
#     right = len(items) - 1

#     while (left <= right):
#         middle = (left + right) // 2

#         if value == items[middle]:
#             return middle

#         if value < items[middle]:
#             right = middle - 1
#         else:
#             left = middle + 1

#     return -1


# items = [-3, -1, 1, 3, 5, 7, 9, 11]
# print(binary_search(items, 100))  # => -1
# print(binary_search(items, -1))  # => 1
# print(binary_search(items, 7))  # => 5


# def hanoi(height, start, to):
#     if height == 1:
#         print(f'с {start} на {to}')
#         return

#     temporary = 6 - start - to
#     hanoi(height - 1, start, temporary)
#     print(f'с {start} на {to}')
#     hanoi(height - 1, temporary, to)

# hanoi(4, 1, 2)

# s = 'ABRAKADABRA'
# print(s[-5:-10:-1])  # 'DAKAR'

# source = [1, 10, 100, 2, 20, 200]


# a = sum(map(lambda num: num ** 2, (filter(lambda num: num // 10 >= 1 and num // 10 < 10, source))))

# b = sum([x ** 2 for x in [num for num in source if num // 10 >= 1] if x // 10 < 10])

# c = sum([num ** 2 for num in source if num // 10 >= 1 and num // 10 < 10])

# d = [num += num ** 2 for num in source if num // 10 >= 1 and num // 10 < 10]

# print(d)



# xs = [1, 3, 5]
# ys = list(range(6, 20))

# print(id(xs))
# list(map(xs.append, filter(lambda y: y % 2 == 1, ys)))

# # [xs.append(y) for y in ys if y % 2 == 1]

# # xs.extend(filter(lambda y: y % 2 == 1, ys))

# # xs.extend([y for y in ys if y % 2 == 1])

# print(xs)

# print(id(xs))

# squares = {x * x for x in range(10)}
# print(squares)

# char_positions = {char: pos for pos, char in enumerate("Hello, World!")}
# print(char_positions)

# squares = {x: x ** 2 for x in range(10)}
# print(squares)
# # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# print({'a': v for v in (1, 2)})

# {print("Hello") for _ in range(3)}


# a = [(1,2),(3,4),(5,6),(4,3),(2,1)]
# print(dict(set(a)))


# def print6(xs):
#     for i, x in enumerate(xs):
#         print(x)
#         if i == 5:
#             break

# i = (x * x for x in range(10))
# print6(i)
# # => 0
# # => 1
# # => 4
# # => 9
# # => 16
# # => 25
# print6(i)  # Продолжаем перебирать элементы
# # => 36
# # => 49
# # => 64
# # => 81
# print6(i)  # Больше ничего не осталось

# print(any(x > 100 for x in range(1000000)))


# any(print(x) for x in (1, 2, 3))


# (print(x) for x in (1, 2, 3))


# {0: print(x) for x in (1, 2, 3)}


# [print(x) for x in (1, 2, 3)]


# {print(x) for x in (1, 2, 3)}


# {print(x): 0 for x in (1, 2, 3)}

# print(list(range(3)))

# {print(x, "Hello") for x in range(3)}

###########################
# import math

# def make(numer, denom):
#     # a = numer
#     # b = denom
#     # while b != 0:
#     #     a, b = b, a % b
#     # gcd = a
#     # print(gcd)
#     gcd = math.gcd(numer, denom)
#     return {'numer': int(numer/gcd), 'denom': int(denom/gcd)}

# num = make(1, 3)

# def get_numer(num):
#     return num['numer']

# def get_denom(num):
#     return num['denom']

# def add(rat1, rat2):
#     if get_denom(rat1) == get_denom(rat2):
#         return make(get_numer(rat1) + get_numer(rat2), get_denom(rat1))
#     else:
#         return make((get_numer(rat1)*get_denom(rat2)) +
#                     (get_numer(rat2)*get_denom(rat1)),
#                      get_denom(rat1)*get_denom(rat2))
#     # return result
#     # else:
#     #     nok = get_denom(rat1) * get_denom(rat2)
#     #     result = {'numer': get_numer(rat1) + get_numer(rat2), 
#     #               'denom': get_denom(rat1)}
#     #     # gcd = math.gcd(get_denom(rat1), get_denom(rat2))
#     #     # multiply = get_denom(rat1) * get_denom(rat2)
#     #     # nok = multiply/gcd


# def sub(rat1, rat2):
#     if get_denom(rat1) == get_denom(rat2):
#         return make(get_numer(rat1) - get_numer(rat2), get_denom(rat1))
  

# print(make(3, 9))
# print(add(make(-1, 4), make(12, 5)))
# print(sub(make(3, 9), make(10, 3)))
# print(add(make(3, 9), make(10, 3)))

##############################
from urllib.parse import urlparse
def make(url):
    # parsed_url = urlparse(url)
    return urlparse(url)

u = make('https://hexlet.io/community?q=low')

print(u)
#####################################

# s = "Hello, world!"
# m = 'wold'
# index = s.find("world")
# print(index)  # выводит 7
# print(m in s)

#################################
import os
path1 = "/home/user"
path2 = "documents"
# filename = "example.txt"

# Joining the paths
full_path = os.path.join(path1, path2)

print(full_path)

######################################

def set_(path, key, value):
    with open(path, 'r+') as f:
        f.seek(0)
        lines = f.readlines()
        pos = None
        # если файл не пустой, то проводится поиск существующего ключа
        if len(lines) != 0:
            for line in lines:
                k, v = line.strip().split('\t')
                print(k, v)
                if k == key:
                    pos = f.tell() - len(v)
                    break
            else:
                f.write(f"{key}\t{value}\n")
        # если файл пустой, то записывается строка ключ\значение
        else:
            f.write(f"{key}\t{value}\n")
            return
        if pos is not None:
            f.seek(pos)
            f.write(value)


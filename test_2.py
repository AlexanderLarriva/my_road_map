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

def decorator_1(func):
    print('декоратор 1')
    
    def wrapper():
        print('перед функцией')
        func()
    return wrapper

def decorator_2(func):
    print('декоратор 2')
    
    def wrapper():
        print('перед функцией')
        func()
    return wrapper

@decorator_1
@decorator_2
def basic_1():
    print('basic_1')

@decorator_1
def basic_2():
    print('basic_2')

print('>> старт')
basic_1()
basic_2()
print('>> конец')


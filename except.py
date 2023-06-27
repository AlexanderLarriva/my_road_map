# def decorator(func):
#     def wrapper():
#         print("До вызова функции")
#         func()
#         print("После вызова функции")
#     return wrapper

# @decorator
# def say_hello():
#     print("Привет!")

# say_hello()


# def suppress(func):
#     def wrapper():
#         print("До вызова функции")
#         func()
#         print("После вызова функции")
#     return wrapper


# @suppress(ZeroDivisionError, or_return=42)
# def foo():
#      return 1 // 0
 
# foo()  # 42
 
# @suppress((KeyError, IndexError))
# def get_item(key, structure):
#      return structure[key]
 
# get_item(7, "foo") is None  # True
# get_item('a', {}) is None  # True

def decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Аргументы декоратора:", arg1, arg2)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@decorator_with_args("Аргумент 1", "Аргумент 2")
def say_hello(name):
    print("Привет,", name)

say_hello("Alice")

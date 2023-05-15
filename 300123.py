def call_twice(function, *args, **kwargs):
    a = function(*args, **kwargs)
    b = function(*args, **kwargs)
    return (a, b) 

def count(*args, **kwargs):
    return args, kwargs

a = call_twice(count, 12, value=42)
print(type(a))
print(list(a))
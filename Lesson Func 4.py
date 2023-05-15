def call_twice(function):
    def inner(argument):
        return function(function(argument))
        # return function(argument)
    return inner

def result(*args):
    return args

print(call_twice(result)("Hello", "Ivan"))
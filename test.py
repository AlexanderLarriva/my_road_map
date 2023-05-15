def double(function):
    def inner(argument):
        return function(function(argument))
        # return function(argument)
    return inner

def multiply_by_five(x):
    return x * 5

print(double(multiply_by_five)(3))

multiply_by_25 = double(multiply_by_five)
multiply_by_25
# <function double.<locals>.inner at 0x7fd1975c58c8>
print(multiply_by_25(1))
# 25
multiply_by_625 = double(multiply_by_25)
multiply_by_625
# <function double.<locals>.inner at 0x7fd1968f41e0>
print(multiply_by_625(1))
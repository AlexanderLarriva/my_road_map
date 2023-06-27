# def get_unique(*args):
#     result = set()
#     for arg in args:
#         for i in arg:
#             result.add(i)
#     return list(result)


# print(get_unique([1, 2, 3], [3, 4, 5], [5, 6, 7]))  # [1, 2, 3, 4, 5, 6, 7]

########################################
import math

def get_square_roots(value):
    result = []
    if value > 0:
        result.append(-math.sqrt(value))
        result.append(math.sqrt(value))
    elif value == 0:
        result.append(0)
    else:
        return result
    return result


# a = 25
# print(math.sqrt(25))

print(get_square_roots(25))  # [-5.0, 5.0]
print(get_square_roots(0))  # [0]
print(get_square_roots(-25))  # []
# def each2d(test, matrix):
    
#     return (test(inner_elem) for inner_elem in sublist for sublist in matrix)

def each2d(test, matrix):
    return all(test(inner_elem) for sublist in matrix for inner_elem in sublist)

def some2d(test, matrix):
    return any(test(inner_elem) for sublist in matrix for inner_elem in sublist)

def sum2d(test, matrix):
    return sum(inner_elem for sublist in matrix for inner_elem in sublist if test(inner_elem))


def is_int(x):
    return isinstance(x, int)

def is_even(x):
    return x % 2 == 0


# a = each2d(is_int, [1,2,3,4,5])
# print(list(a))

# a = each2d(is_int, [[1, ""], 
#                 [3, 4]])

# print(a)

# b = some2d(is_int, [["", ""], 
#                 ["", ""]])

# print(b)

c = sum2d(is_even, [[1, 2], 
                [3, 4]])

print(c)
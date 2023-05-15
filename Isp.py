# def is_continuous_sequence(MyList):
#   if len(MyList) == 0:
#     return False
#   for index in range(len(MyList)-1):
#     if MyList[index + 1] - MyList[index] != 1:
#        return False
#   return True
  
# print(is_continuous_sequence([1]))

# def is_continuous_sequence(source):
#     if len(source) < 2:
#         return False
#     for x, y in zip(source, source[1:]):
#         if (y - x) != 1:
#             return False
#     return True
  
  
# print(is_continuous_sequence([1,2,3,4]))

# import operator
from functools import reduce
from operator import getitem, truth, add


# def keep_truthful(source): #filter
#   result = []
#   for i in source:
#     if operator.truth(i):
#       result.append(i)
#   return result

def keep_truthful(items):
    return filter(truth, items)

print(list(keep_truthful((True, False, "", "foo"))))

# list(filter(keep_truthful, [True, False, "", "foo"]))

# def abs_sum(items): #map
#   result = []
#   for i in items:
#     result.append(abs(i))
#   return sum(result)

def abs_sum(numbers):
    return sum(map(abs, numbers))




print(abs_sum([-3, -7]))


# print(reduce(abs_sum, [-3, -7]))


# def walk(MyDict, itersource): #reduce
#   result = MyDict
#   for i in itersource:
#     result = getitem(result, i)
#   return result

def walk(dictionary, path):
    return reduce(getitem, path, dictionary)

print(walk({'a': {7: {'b': 42}}}, ["a"]))
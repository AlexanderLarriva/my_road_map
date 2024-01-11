# Реализуйте функцию merged(), которая объединяет несколько словарей в один общий словарь. 
# Функция принимает список словарей и возвращает результат в виде словаря, 
# в котором каждый ключ содержит множество (set) уникальных значений.

Dict1 = {'a': 1, 'b': 2}
Dict2 = {'b': 10, 'c': 100}
Res = {'a': {1}, 'b': {2, 10}, 'c': {100}}

List_of_Dicts = [Dict1, Dict2]


# def merged(List_of_Dicts):
#     Result = {}
#     for Dict in List_of_Dicts:
#         for key, value in Dict.items():
#             if key not in Result:
#                 Result[key] = set()
#                 Result[key].add(value)
#             Result[key].add(value)
#     return Result
from collections import defaultdict


def merged(dicts):
    aggregate = defaultdict(set)
    for source in dicts:
        for key, value in source.items():
            aggregate[key].add(value)
    return aggregate

print(merged(List_of_Dicts))
A, B, C, D = 'abcd'

print(merged([
        {A: 1},
        {B: 2},
        {C: 3},
    ]
    ))

print(
    merged([
        {A: 1},
        {A: 2},
        {A: 3},
    ]
))


print(merged([
        {A: 1, B: 2},
        {B: 3, C: 4},
        {C: 5, D: 6},
    ]))

# merged([
#         {A: 1},
#         {B: 2},
#         {C: 3},
#     ]
#     ) 


# {
#         A: {1},
#         B: {2},
#         C: {3},
#     }
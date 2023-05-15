def select_odd(func, lst):
    # проход по "верхнему" списку
    for index_up_lst in range(len(lst)-1, -1, -1): # перебираем список в обратном порядке
        if func(index_up_lst): # если индекс не четный
            lst.pop(index_up_lst) # удаляем его
    # проход по "вложенному" списку
    for index_inner_lst in lst: 
        # print(type(i), i) проверить тип i - это вложенный список
        for j in range(len(index_inner_lst)-1, -1, -1): # перебираем список в обратном порядке
            if func(j): # если индекс не четный
                index_inner_lst.pop(j) # удаляем его

def is_even(x):
    if x%2 != 0:
        return True

# lst = [
#         [1, 2, 3, 4, 5],
#         ['c', 'a', 't'],
#         ['d', 'o', 'g'],
#         [100, 200, 300, 400],
#         [True, False],
#         [],
#         [],
#     ]

# select_odd(is_even, lst)
# print(select_odd(lst))

# backup = list(map(lambda x: x[:], lst))
# print(backup)


lst = [[1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9], 
       [10, 11, 12]]

# print(lst[::-1])

# print(lst)

# lst = [1, 2, 3, 4, 6, 9, 7, 4]





# def is_even_list(x):
#     for i in x:
#         if x.index(i) % 2 != 0:
#             return True
        
def odds_from_odds(lst):
    return list(map(lambda lst: lst[::2], lst[::2]))


# def odds_from_odds(lst):
#     def odd_filter(n):
#         return n % 2 != 0
#     odd_lists = [list(filter(odd_filter, sub_lst)) for i, sub_lst in enumerate(lst) if i % 2 == 0]
#     return odd_lists



selection = odds_from_odds(lst)

print(selection)



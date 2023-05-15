def select_odd(lst):
    # проход по "верхнему" списку
    for index in range(len(lst)-1, -1, -1): # перебираем список в обратном порядке
        if not lst[index]: # если индекс не четный
            lst.pop(index) # удаляем его
    # проход по "вложенному" списку
    for index_inner in lst: 
        # print(type(i), i) проверить тип i - это вложенный список
        for j in range(len(index_inner)-1, -1, -1): # перебираем список в обратном порядке
            if not index_inner[j]: # если индекс не четный
                index_inner.pop(j) # удаляем его

lst = [[1, 2, 3], 
       [4, False, ""], 
       [], 
       [10, 0, 12]]

select_odd(lst)
print(lst)


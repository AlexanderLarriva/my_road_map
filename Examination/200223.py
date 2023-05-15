# def keep_odds_from_odds(Mylist):
#     filtered_list = []
#     # Проходим по каждому списку внутри основного списка
#     for inner_list in Mylist:
#         # Создаем пустой список для хранения четных элементов текущего списка
#         filtered_inner_list = []
#         # Проходим по каждому элементу текущего списка и проверяем его на четность
#         if Mylist.index(inner_list) %2 == 0:
#             for element in inner_list:
#                 if element % 2 != 0:
#                     filtered_inner_list.append(element)
#             # Добавляем отфильтрованный список в список отфильтрованных списков
#             filtered_list.append(filtered_inner_list)
#     print(filtered_list)

        
def keep_odds_from_odds(lst):
    odds = []
    for i in range(len(lst)):
        if i % 2 == 0:
            # сохраняем нечетные числа из текущего списка
            for j in range(len(lst[i])-1, -1, -1):
                if lst[i][j] % 2 == 0:
                    lst[i].pop(j)
            # добавляем нечетные числа в результирующий список
            odds.extend(lst[i])
        else:
            # удаляем все числа из текущего списка
            lst[i] = []
    # очищаем исходный список от пустых вложенных списков
    lst[:] = [x for x in lst if x]
    # очищаем список нечетных чисел от четных
    for i in range(len(odds)-1, -1, -1):
        if odds[i] % 2 == 0:
            odds.pop(i)
    # return odds
    
    
l = []    


print(keep_odds_from_odds(l))

print(l)
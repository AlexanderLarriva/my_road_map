def non_empty_truths1(lst):
    return [[elem for elem in inner_lst if elem] for inner_lst in lst if any(inner_lst)]


def non_empty_truths(source):
    
    return [item for item in [[elem 
            for elem in sublst # проверяем внешние списки
                if elem] 
                for sublst in source 
                    if sublst]
            if item      
    ]
    
    
def non_empty_truths2(list_of_lists):
    return [
        truths for truths in
        [[elem for elem in one_list if elem]  # noqa: WPS335
         for one_list in list_of_lists
         ]
        if truths
    ]
    
Lists = [[1,2,0], [0, ""], [False, None], []]

# Lists =[[0],[0],[0]]

a = non_empty_truths1(Lists)
print(type(a))
print(a)



# List_of_lists = [0, 1, "", True, 2, "3", False, {}]


# print([x for x in List_of_lists if x])



# print([[item for item in sublst if item] for sublst in List_of_lists if sublst])

# print(id(List_of_lists))




# print(List_of_lists is a) # False


# v = '1'

# print(v is True)
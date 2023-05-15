def keep_odds_from_odds(Mylist):
    
    print(Mylist[::2])
    # for i in range(len(Mylist)):
    #     Mylist[i] = Mylist[i][::2]
    # l = Mylist
    # print(Mylist)
    
    
    
# def keep_odds_from_odds(Mylist):
    
#     for i in reversed(Mylist):
#         if len(Mylist) % 2 == 0:
#             Mylist[i].remove()
#     print(Mylist)
    
    
  
    
    # for i in range(len(Mylist)):
    #     Mylist[i] = Mylist[i][::2]
    # l = Mylist
    # print(Mylist)
        
    
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]    
# print(l) 


# c = [i for i in l]

# print(c)



keep_odds_from_odds(l)
print(l)

# get_value = lambda pair: pair[1]  # noqa: E731
    
    # return list(map(get_value, (filter(is_odd_position, enumerate(source)))))
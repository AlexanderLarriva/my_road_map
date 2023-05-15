def my_map(func, source):
    for i in source:
        yield func(i)
        
def my_filter(f, xs):
    yield (i for i in xs if f(i))

# def my_filter(func, source):
#     for i in source:
#         if func(i):
#             yield i
            
def replicate_each(n, xs):
    # count = 0
    for i in xs:
        count = 0
        while count < n:
            yield i
            count += 1


# nums = [1, 2, 3, 4, 5]
# squared_nums = my_map(lambda x: x ** 2, nums)
# print(list(squared_nums)) # [1, 4, 9, 16, 25]


print(list(my_filter(lambda x: x % 2 == 1, range(10))))  # [1, 3, 5, 7, 9]
# print(list(replicate_each(1, [1, 'a'])))  # [1, 'a']
print(list(replicate_each(3, [1, 'a'])))  # [1, 1, 1, 'a', 'a', 'a']
print(list(replicate_each(0, [1, 'a'])))  # []
# def reverse(string):
#     """Reverse string

#     >>> reverse('')
#     ''

#     >>> reverse('Hexlet')
#     'telxeH'
#     """

#     return string[::-1]

# # Нужно для запуска тестов
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()


# def invert_case(string):
#     # BEGIN (write your solution here)
#     """Invert case
    
#     >>> invert_case('')
#     ""
    
#     >>> invert_case('A')
#     'a'
    
#     >>>invert_case('a')
#     'A'
#     """
#     # END

#     result = ''
#     for char in string:
#         result += char.swapcase()
#     return result


# if __name__ == "__main__":
#     import doctest
#     failed, attempted = doctest.testmod()
#     assert failed == 0
#     assert attempted == 3


# # print(invert_case("1"))

##############################

# def index_of(coll, value, from_index=0):
#     length = len(coll)

#     if length == 0:
#         return -1

#     index = from_index

#     if index < 0:
#         if index < -length:
#             index = 0
#         else:
#             index += length

#     try:
#         return coll.index(value, index)
#     except ValueError:
#         return -1
    
    
# print(index_of([1,2,3,3,2], 2, -3))

########################################

# def my_slice(coll, start=0, end=None):
#     length = len(coll)

#     normalized_end = length if end is None else end

#     if length == 0:
#         return []

#     normalized_start = start

#     if normalized_start < 0:
#         if normalized_start < -length:
#             normalized_start = 0
#         else:
#             normalized_start += length

#     return coll[normalized_start:normalized_end]

# print(my_slice([1,2,3,3,2], -3))


#####################################
# def get_mid_point(point1, point2):
#     return {'x': (point1['x'] + point2['x'])/2,
#             'y': (point1['y'] + point2['y'])/2}


# point1 = {'x': 0, 'y': 0}
# point2 = {'x': 4, 'y': 4}
# print(get_mid_point(point1, point2))  # {'x': 2, 'y': 2}

####################################################

# def make_segment(point1, point2):
#     segment = {'point1': point1,
#                'point2': point2} 
#     return segment



# point1 = {'x': 0, 'y': 0}
# point2 = {'x': 4, 'y': 4}

# print(make_segment(point1, point2))

# def get_mid_point_of_segment(segment):
#     return {'x': (segment['point1']['x'] + segment['point2']['x'])/2,
#             'y': (segment['point1']['y'] + segment['point2']['y'])/2}

# print(get_mid_point_of_segment(make_segment(point1, point2)))


# def get_begin_point(segment):
#     return {"x": segment['point1']['x'],
#             "y": segment['point1']['y']}
    
# print(get_begin_point(make_segment(point1, point2)))

#########################################

# from points import get_x, get_y, make_decart_point


# BEGIN (write your solution here)
# def make_segment(point1, point2): # создать отрезок
#     return {"begin_point": point1, "end_point": point2}


# def get_begin_point(segment):
#     return segment["begin_point"] # получить начальную точку


# def get_end_point(segment):
#     return segment["end_point"] # получить конечную точку

# def make_decart_point(x, y):
#     return {"x": x, "y": y}

# def get_x(point):
#     return point["x"]

# def get_y(point):
#     return point["y"]

# def get_mid_point_of_segment(segment): # получить срединную точку
#     begin_point = get_begin_point(segment)
#     end_point = get_end_point(segment)

#     x = (get_x(begin_point) + get_x(end_point)) / 2
#     y = (get_y(begin_point) + get_y(end_point)) / 2
    

#     return make_decart_point(x, y)


# segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))

# print(segment)


######################
def make_decart_point(x, y):
    return {"x": x, "y": y}

def get_x(point):
    return point["x"]

def get_y(point):
    return point["y"]

def get_start_point(x, y):
    return make_decart_point(x, y)


def make_rectangle(left_top, width, height):
    return {'A': left_top, 
            'B': make_decart_point(get_x(left_top) + width, get_y(left_top)), 
            'C': make_decart_point(get_x(left_top), get_y(left_top) - height), 
            'D': make_decart_point(get_x(left_top) + width, get_y(left_top) - height)}

rectangle = make_rectangle(get_start_point(4, 4), 4, 2)

print(rectangle)
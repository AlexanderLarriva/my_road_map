# def rgb(red, green, blue):
#     return red, green, blue

# class Color():
#     red = rgb(255, 0, 0)
#     green = rgb(0, 255, 0)
#     blue = rgb(0, 0, 255)


# a = Color.red

# print(a)
# print(Color.green)
# print(Color.blue)

###################################################


# class RGB:
#     # в случае иммутабельных значений можно себе позволить
#     # сделать так
#     red = green = blue = 0


# red, green, blue = RGB(), RGB(), RGB()
# red.red = 255
# green.green = 255
# blue.blue = 255

# print(blue.blue)


# def rgb2tuple(rgb):
#     if isinstance(rgb, RGB):
#          return rgb.red, rgb.green, rgb.blue
 
# rgb2tuple(42)
# rgb2tuple(RGB.red)  # (255, 0, 0)
# print(rgb2tuple(RGB.green))  # (0, 255, 0)
# rgb2tuple(RGB.blue)  # (0, 0, 255)

##################################################

# class Counter():
#     value = 0
#     def inc(self, count = 1):
#         self.value += count
#         return self.value
#     def dec(self, count = 1):
#         self.value -= count
#         if self.value < 0:
#             self.value = 0
#         return self.value



# c = Counter()
# print(c.inc())
# print(c.inc())
# # c.inc()
# print(c.inc(40))
# print(c.value)  # 42
# print(c.dec())
# print(c.dec(1000))
# # c.value  # 11
# # c.dec(delta=100)
# # c.value  # 0

#####################################

class Counter:
    def __init__(self, initial_value=0):
        self._value = initial_value

    def inc(self, delta=1):
        return Counter(self._value + delta)

    def dec(self, delta=1):
        new_value = self._value - delta
        if new_value < 0:
            new_value = 0
        return Counter(new_value)

    @property
    def value(self):
        return self._value


c = Counter()
print(c.inc().inc(5).dec(2).value)  # 4
 
# # Старый экземпляр не должен изменяться
# d = c.inc(100)
# d.dec().value  # 99
 
# forty_two = Counter(42)
# forty_two.value  # 42
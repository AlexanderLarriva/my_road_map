# class Person:
#     pass
 
# bob = Person()


# print(bob.__class__ is Person)

# print(isinstance(bob, Person))

# print(bob == Person)

# print(bob is Person)
###################################################### VAR 1
# class RGB:
#     def __init__(self, red=0, green=0, blue=0):
#         self.red = red
#         self.green = green
#         self.blue = blue

# red = RGB(red=255)
# green = RGB(green=255)
# blue = RGB(blue=255)
#########################################################
class RGB:
    red = 0
    green = 0
    blue = 0

red = RGB()
print(red)
print(red.red)
red.red = 255
green = RGB()
green.green = 255

blue = RGB()
blue.blue = 255



def rgb2tuple(rgb):
    if isinstance(rgb, RGB):
         return rgb.red, rgb.green, rgb.blue
 


a = rgb2tuple(42)
r = rgb2tuple(red)  # (255, 0, 0)
g = rgb2tuple(green)  # (0, 255, 0)
b = rgb2tuple(blue)  # (0, 0, 255)

print(a)
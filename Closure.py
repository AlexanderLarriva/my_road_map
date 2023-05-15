# def make_closure():
#   y = 1
#   def inner(x):
#     return x + y
#   y = 42
#   return inner

# print(make_closure()(100))

# printers = []
# for i in range(10):
#   def printer():
#     print(i)
#   printers.append(printer)
  
# printers[0]()
# # 9
# printers[5]()
    
# printers = []
# for i in range(10):
#   def make_printer(arg):
#     def printer():
#       print(arg)
#     return printer
#   p = make_printer(i)
#   printers.append(p)

# printers[0]()
# # 0
# printers[5]()


# name ='Bob'

# def make_closure():

#   name = 'Alice'

#   def inner():
#     print('Hello', name)

#   name = 'Grace'

#   return inner

# name = 'Thomas'

# make_closure()()


def f():
    x = 1
    def g():
        return x
    x = 2
    def h():
        return x
    x = 3
    return g() == h(), g() + h()
 
print(f()) # ???
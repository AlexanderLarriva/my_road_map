def greet(name, *args):
  # print("Hello, " + " and ".join((name, ) + args) + "!")
  return ("Hello, " + " and ".join((name, ) + args) + "!")
  # for n in (name, ) + args:
  #   # return ','.join(n)
  #   print(f'Hello, {n}!')


# print(greet('Ivan', 'Oleg', 'Petr'))
greet('Ivan', 'Oleg', 'Petr')
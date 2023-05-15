def greet(name, surname):
  return f'Hello, {name} {surname}!'


def partial_apply(func, name):
  def inner(surname):
    return func(name, surname)
  return inner


def flip(func):
  def inner(*args):
    Surname, Name = args
    return func(Name, Surname)
  return inner


v = flip(greet)
print(v('Christian', 'Teodor'))

f = partial_apply(greet, 'Dorian')
print(f('Grey'))
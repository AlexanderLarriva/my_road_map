def memoized(func):
  '''
  Function - decorator.
  
  Demonstrates how closures and the decorator function work.
  '''
  d = {}

  def inner(arg):
    if arg in d:
      return d[arg]
    else:
      d[arg] = func(arg)
    return d[arg]
  return inner


@memoized
def f(x):
    print('Calculating...')
    return x * 10
 
print(f(1))
print(f(2))
print(f(1))

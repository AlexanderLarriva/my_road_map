# import collections

def memoizing_decor(count = 1):
  def memo(func):
    # d = collections.OrderedDict()
    d = {}
    bank = []
    def inner(arg):
      if len(d) >= count:
        if arg in d:
          return d[arg]
        else:
          d[arg] = func(arg)
        return d[arg]
      else:
        d.pop(arg)
        return d
        
    return inner
  return memo

@memoizing_decor(count = 2)
def f(x):
    print('Calculating...')
    return x * 10
 
print(f(1))
print(f(2))
print(f(1))
print(f(4))
print(f(5))
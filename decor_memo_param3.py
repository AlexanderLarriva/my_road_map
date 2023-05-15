from functools import wraps

def memoized(function):
  '''Function - decorator'''
  My_dict = {}
  # def wrapper

  def inner(arg):
    memoized_result = My_dict.get(arg)
    if memoized_result is None:
      memoized_result = function(arg)
      My_dict[arg] = memoized_result
    return memoized_result
  return inner
  
  
@memoized
def f(x):
    print('Calculating...')
    return x * 10
 
print(f(1))
print(f(2))
print(f(1))
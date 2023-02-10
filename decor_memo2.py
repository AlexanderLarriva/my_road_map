def memoized(function):
  '''Function - decorator
  
  Demonstrates how closures and the decorator function work.'''
  memory = {}

  def inner(argument):
    memoized_result = memory.get(argument)
    if memoized_result is None:
      memoized_result = function(argument)
      memory[argument] = memoized_result
    return memoized_result

  return inner
  
  
@memoized
def f(x):
    print('Calculating...')
    return x * 10
 
print(f(1))
print(f(2))
print(f(1))
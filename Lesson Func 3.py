def updated(MyDict, **kwargs):
  NewDict = MyDict.copy()
  NewDict.update(kwargs)
  return NewDict


d = {'a': 1, 'b': False}
# print(d)
updated(d, a=2, b=True, c=None, f=123)
# print(d)
print(updated(d) == d)
print(updated(d) is d)
def toggle(READ_ONLY, MySet):
  if READ_ONLY in MySet:
    MySet.discard(READ_ONLY)
  else:
    MySet.add(READ_ONLY)


def toggled(READ_ONLY, MySet):
  NewSet = MySet.copy()
  toggle(READ_ONLY, NewSet)
  return NewSet

MySet = set([1, 2, 2, 3, 4, "read_only"])
READ_ONLY = "read_only"
toggle(READ_ONLY, MySet)

print(toggled(READ_ONLY, MySet))

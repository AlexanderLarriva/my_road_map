def all_unique(iter_elem):
  if not iter_elem:
    return True
  items = list(iter_elem)
  MySet = set(items)
  a = len(items)
  b = len(MySet)
  if a == b:
    return True
  else:
    return False


print(all_unique(['spam', 'egg']))
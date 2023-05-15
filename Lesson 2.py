import collections

def all_unique(iter_elem):
  if iter_elem is None:
    return True
  #c = collections.defaultdict(int)
  c = collections.Counter(iter_elem)
  # for elem in iter_elem:
  #   c[elem] += 1
  print(c)
  for elem in c:
    if c[elem] > 1:
      return False
    else:
      return True
    
print(all_unique(['spam', 'egg', 'spam', 'counter', 'counter', 'counter']))

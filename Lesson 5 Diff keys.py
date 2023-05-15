def diff_keys(Old_dict, new_dict):
  set1 = set(Old_dict)
  set2 = set(new_dict)
  return {'kept': set(set1 & set2), 'added': set(set2 - set1), 'removed': set(set1 - set2)}


print(diff_keys({'a': 1, 'b': 2, 'c': 3, 'e': 5}, {'a': 1, 'b': 2, 'c': 3, 'd': 4}))
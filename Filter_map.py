def filter_map(function, MyList):
  result = []
  for item in MyList:
    keep, value = function(item)
    # if keep is True:
    if keep:
      result.append(value)
  return result


def map(value):
  if value > 0:
    return True, value
  return False, None
    
INITIAL_ASCII_CODE = 65
FINAL_ASCII_CODE = 90

def is_latin(value):
  if ord(value.upper()) in range(INITIAL_ASCII_CODE, FINAL_ASCII_CODE+1):
    return True, value.upper()
  return False, None

print(filter_map(is_latin, "HрYujЛIoПzРнLs"))

# print(filter_map(map, [1, 2, -5, -5, 2]))
  




# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result

# print(map(str, range(5)))
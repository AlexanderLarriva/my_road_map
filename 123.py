def get_first_name(fullname):
    return fullname.split('_')[0]


def sort_by(key, coll):
  coll_copy = coll[:]
  coll_copy.sort(reverse=True, key=key)
  return coll_copy

users = ["Michail_Bulgakov", "Alex_Puskin", "Dmitrii_Donskoy"]

# print(get_first_name("Dmitrii_Donskoy"))
 
print(sort_by(get_first_name, users)) 
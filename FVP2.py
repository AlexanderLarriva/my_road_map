# def get_first_name(name):
#   return name.split("_")[0]
  


# def sort_by(function, name_list):
#   names_copy = name_list[:]
#   names_copy.sort(key=function)
#   print('Копия списка: ', names_copy)
#   return names_copy 

def get_first_name(fullname):
  
  return fullname.split('_')[0]


def sort_by(key, coll):
  coll_copy = coll[:]
  coll_copy.sort(key=key)
  return coll_copy

# users = ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]
users = ["Michail_Bulgakov", "Alex_Puskin", "Dmitrii_Donskoy"]

names = ["Obi-Wan_Kenobi", "Jabba_Hutt", "Princess_Leia"]


print(get_first_name("Dmitrii_Donskoy"))  # Vader
 
print(sort_by(get_first_name, users))  # ["Boba_Fett", "Luke_Skywalker", "Vader_Darth"]

# print(users) # => ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"] 
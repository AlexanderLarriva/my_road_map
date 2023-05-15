def get(collection, key, default_value = None):
    return collection.get(key, default_value)




get({"hello": "world"}, "hello")  # world
get({"hello": "world"}, "hello", "kitty")  # world
get({}, "hello", "kitty")  # kitty
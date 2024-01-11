def count_words(path):
    Dict_words = {}
    with open(path, "r") as file:
        content = file.read()
    words = content.lower().split()
           
    for i, word in enumerate(words):
        if word[-1] in [',', '!', '.', '?']:
            words[i] = word[:-1]
            
    for word in words:
        if word in Dict_words:
            Dict_words[word] += 1
        else:
            Dict_words[word] = 1
    return Dict_words




print(count_words('/home/larriva/MyTraning/python.txt'))
 
# {
#  'the': 2,
#  'python': 2,
#  'after': 2,
#  'language': 1,
#  'was': 1,
#  'not': 1,
#  'named': 1,
#  'a': 1,
#  'long': 1,
#  'snake': 1,
#  'but': 1,
#  'british': 1,
#  'comedy': 1,
#  'show': 1,
#  'monty': 1,
#  'flying': 1,
#  'circus': 1
# }
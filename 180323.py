from hexlet import fs

# Вторым параметром mkdir принимает список потомков,
# которые могут быть либо созданными mkdir директориями, либо созданными mkfile файлами
tree = fs.mkdir('etc', [
    fs.mkfile('bashrc'),
    fs.mkdir('consul', [
        fs.mkfile('config.json'),
    ]),
])

def print_tree(node, prefix=''):
    print(prefix + fs.get_name(node))
    if fs.is_directory(node):
        for child in fs.get_children(node):
            print_tree(child, prefix + '    ')

# print_tree(tree)

# print(tree)
print(fs.flatten(tree))

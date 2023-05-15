


# def remove_first_level(tree):
#     second_level_tree = []
#     for elem in tree:
#         if isinstance(elem, list):
#             for sub_elem in elem:
#                 second_level_tree.append(sub_elem) 
#     return second_level_tree

########################################
# def remove_first_level(tree):
#     return [sub_elem 
#                 for elem in tree if isinstance(elem, list)
#                     for sub_elem in elem]

# tree1 = [[5], 1, [3, 4]]
# print(remove_first_level(tree1))  # [5, 3, 4]
# tree2 = [1, 2, [3, 5], [[4, 3], 2]]
# print(remove_first_level(tree2))  # [3, 5, [4, 3], 2]


################################################

# from hexlet import fs

# Вторым параметром mkdir принимает список потомков,
# которые могут быть либо созданными mkdir директориями, либо созданными mkfile файлами
# tree = fs.mkdir('etc', [
#     fs.mkfile('bashrc'),
#     fs.mkdir('consul', [
#         fs.mkfile('config.json'),
#     ]),
# ])

# print(tree)

###################

# from hexlet import fs

# def generate():
#     return fs.mkdir('python-package', 
#                     [fs.mkfile('Makefile'),
                     
#                     fs.mkfile('README.md'),
                    
#                     fs.mkdir('dist'),
                    
#                     fs.mkdir('tests', 
#                             [fs.mkfile('test_solution.py')]),
                    
#                     fs.mkfile('pyproject.toml'),
                    
#                     fs.mkdir('.venv', 
#                             [fs.mkdir('lib', 
#                                [fs.mkdir('python3.6', 
#                                  [fs.mkdir('site-packages', 
#                                     [fs.mkfile('hexlet-python-package.egg-link')])])])], 
#                             {'owner': 'root', 'hidden': False})],
#                     {'hidden': True})
#     # return tree
    
# print(generate())

########################################

from hexlet import fs

import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile

def compress_images(tree):
        files = get_children(tree)
        print('files: ', files)
        # new_tree = {}
        for file in files:
            # print(type(fs.get_name(file)))
            name = get_name(file)
            
            # print(new_meta)
            if is_file(file) and name[name.rfind("."):] == '.jpg':
                new_meta = copy.deepcopy(get_meta(file))
                new_meta['size'] = new_meta['size']//2
                new_file = mkfile(fs.get_name(file), new_meta)
                file = new_file
        return tree
            # return new_file
                        # print(new_file)
                        # get_meta(file).get('size')
                        # print(type(fs.get_name(file)))
        # return file


tree = mkdir(
    'my documents',
    [
        mkfile('avatar.jpg', {'size': 100}),
        mkdir('film', [], {'size': 100}),
        mkfile('photo.jpg', {'size': 150}),
    ],
    {'hide': False}
)

# print(tree)
print(compress_images(tree))
# compress_images(tree)
# {
#     'name': 'my documents',
#     'type': 'directory',
#     'children': [
#         {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
#         {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
#     ],
#     'meta': {'hide': False},
# }

# string = "avatar.jpg"
# extension = string[string.rfind(".") + 1:]
# print(extension)

# string = "avatar.jpg"
# extension = string[string.rfind("."):]
# print(extension)  # выводит ".jpg"


def print_tree(node, prefix=''):
    print(prefix + fs.get_name(node))
    if fs.is_directory(node):
        for child in fs.get_children(node):
            print_tree(child, prefix + '    ')


# print_tree(tree)
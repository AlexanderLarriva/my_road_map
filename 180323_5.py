# import copy

# from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# # BEGIN
# def downcase_file_names(node):
#     new_meta = copy.deepcopy(get_meta(node))
#     name = get_name(node)
#     if is_file(node):
#         return mkfile(name.lower(), new_meta)
#     children = get_children(node)
#     new_children = map(downcase_file_names, children)
#     return mkdir(name, list(new_children), new_meta)
# # END

import copy

from hexlet.fs import get_children, get_meta, get_name
from hexlet.fs import is_directory, mkdir, mkfile


# BEGIN (write your solution here)
def downcase_file_names(tree):
    new_children = []
    for child in get_children(tree):
        if is_directory(child):
            new_child = downcase_file_names(child)
        else:
            new_name = get_name(child).lower()
            new_meta = copy.deepcopy(get_meta(child))
            new_child = mkfile(new_name, new_meta)
        new_children.append(new_child)
    new_meta = copy.deepcopy(get_meta(tree))
    new_tree = mkdir(get_name(tree), new_children, new_meta)
    return new_tree
# END

tree = mkdir('/', [
    mkfile('oNe'),
    mkfile('Two'),
    mkdir('THREE'),
])

# tree = mkdir('/', [
#     mkdir('eTc', [
#         mkdir('NgiNx', [], {'size': 4000}),
#         mkdir(
#             'CONSUL',
#             [mkfile('config.JSON', {'uid': 0})],
#         ),
#     ]),
#     mkfile('HOSTS'),
# ])

new_tree = downcase_file_names(tree)
# new_file = get_children(new_tree)[1]
# get_name(new_file)  # hosts

print(new_tree)
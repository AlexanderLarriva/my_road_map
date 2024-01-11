import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# BEGIN (write your solution here)
def downcase_file_names(tree):
    # сохраняем метаданные
    new_meta = copy.deepcopy(get_meta(tree))
    
    children = get_children(tree)
    for child in children:
        name = get_name(child)
        if is_file(child):
            return mkfile(name.lower())
    new_children = map(downcase_file_names, children)
    new_meta = copy.deepcopy(get_meta(tree))
    tree2 = mkdir(get_name(tree), list(new_children), new_meta)
    return tree2

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
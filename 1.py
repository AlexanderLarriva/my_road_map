import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# BEGIN (write your solution here)
def downcase_file_names(tree):
    new_meta = copy.deepcopy(get_meta(tree))
    name = get_name(tree)
    
    if is_file(tree):
        return mkfile(name.lower(), new_meta)
    
    children = get_children(tree)
    new_children = map(downcase_file_names, children)
    return mkdir(get_name(tree), list(new_children), new_meta)


tree = mkdir('/', [
    mkfile('oNe'),
    mkfile('Two'),
    mkdir('THREE'),
])

new_tree = downcase_file_names(tree)

print(new_tree)
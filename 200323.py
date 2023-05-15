from hexlet.fs import mkdir, mkfile, get_children, get_meta, get_name, is_file, is_directory
import copy

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


tree = mkdir('/', [
    mkdir('eTc', [
        mkdir('NgiNx', [], {'size': 4000}),
        mkdir(
            'CONSUL',
            [mkfile('config.JSON', {'uid': 0})],
        ),
    ]),
    mkfile('HOSTS'),
])


print(downcase_file_names(tree))
import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# BEGIN
def downcase_file_names(node):
    new_meta = copy.deepcopy(get_meta(node))
    # print(new_meta)
    name = get_name(node)
    # print(name)
    if is_file(node):
        return mkfile(name.lower(), new_meta)
    children = get_children(node)
    new_children = map(downcase_file_names, children)
    return mkdir(name, list(new_children), new_meta)
# END

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
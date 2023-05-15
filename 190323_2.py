from hexlet.fs import mkdir, mkfile, get_children, get_meta, get_name, is_file, is_directory
# import copy


def downcase_file_names(tree):
    print(get_name(tree))
    
    # if is_directory(tree):
    for child in get_children(tree):
        # if is_file(child):
        #     new_name = get_name(child).lower()
        downcase_file_names(child)
    


tree = mkdir('/', [
    mkdir('eTc', [
        mkdir('NgiNx', [], {'size': 4000}),
        # mkdir(
        #     'CONSUL',
        #     [mkfile('config.JSON', {'uid': 0})],
        # ),
    ]),
    mkfile('HOSTS'),
])


downcase_file_names(tree)
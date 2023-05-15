from hexlet.fs import mkdir, mkfile, get_children, get_meta, get_name, is_file, is_directory
import copy


def compress_images(tree):
    children = get_children(tree)
    new_children = list(map(resize, children))
    new_meta = copy.deepcopy(get_meta(tree))
    return mkdir(get_name(tree), new_children, new_meta)
    


def resize(node):
    # print('node: ', node)
    new_meta = copy.deepcopy(get_meta(node))
    # print('new_meta: ', new_meta)
    name = get_name(node)
    # print(name[-3:])
    if is_file(node):
        if name[-4:] == '.jpg':
            new_meta['size'] = new_meta['size']//2
        return mkfile(name, new_meta)
    return mkdir(get_name(node), get_children(node), new_meta)
 

# tree = mkdir(
#     'my documents',
#     [
#         mkfile('avatar.jpg', {'size': 100}),
#         mkdir('film', [], {'size': 100}),
#         mkfile('photo.jpg', {'size': 150}),
#     ],
#     {'hide': False}
# )

# tree = mkdir('documents', [
#         mkdir('presentations'),
#     ])

tree = mkdir(
        'my documents',
        [
            mkdir('documents.jpg'),
            mkfile('avatar.jpg', {'size': 100}),
            mkfile('passport.jpg', {'size': 200}),
            mkfile('family.jpg', {'size': 150}),
            mkfile('addresses', {'size': 125}),
            mkdir('assets'),
        ],
        {'test': 'haha'},
    )




print(compress_images(tree))

def print_tree(node, prefix=''):
    print(prefix + get_name(node))
    if is_directory(node):
        for child in get_children(node):
            print_tree(child, prefix + '    ')


# print_tree(tree)
from hexlet.fs import mkdir, mkfile, get_children, get_meta, get_name, is_file, is_directory

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 100000}),
])


# подсчет размера файлов внутри директории
def get_files_size(node):
    if is_file(node):
        return get_meta(node)['size']
    children = get_children(node)
    size_list = list(map(get_files_size, children))
    return sum(size_list)


# print(get_files_size(tree))

def du(node):
    children = get_children(node)
    # akk = [(get_name(node), is_file(node))]
    result = []
    for child in children:
        result.append((get_name(child), get_files_size(child)))
    return sorted(result, key=lambda file: file[1], reverse=True)


# map(lambda i:  ,result)
    # Нас интересуют только директории
    # filtered = filter(is_file, children)
    # # Запускаем подсчет для каждой директории
    
    
    # result = map(
    #     lambda child: (get_name(child), get_files_size(child)),
    #     filtered,
    # )
    # return list(result)

print(du(tree))  # [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]

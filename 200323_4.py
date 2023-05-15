from hexlet.fs import mkdir, mkfile, get_children, get_name, is_file


tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('.nginx.conf', {'size': 800}),
        ]),
        mkdir('.consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('.hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])


def get_hidden_files_count(node):
    name = get_name(node)
    if is_file(node):
        if name.startswith('.'):
        # Возвращаем 1 для учета текущего файла
            return 1
    # Если узел — директория, получаем его потомков
    children = get_children(node)
   
    
    counts_hidden_files = list(map(get_hidden_files_count, children))
   
    
    return sum(counts_hidden_files)
    


print(get_hidden_files_count(tree))  # 3
from hexlet import fs

tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkdir('apache'),
        fs.mkdir('nginx', [
            fs.mkfile('nginx.conf'),
        ]),
    ]),
    fs.mkdir('consul', [
        fs.mkfile('config.json'),
        fs.mkfile('file.tmp'),
        fs.mkdir('data'),
    ]),
    fs.mkfile('hosts'),
    fs.mkfile('resolve'),
])



def get_files_count(node):
    if fs.is_file(node):
        return 1
    children = fs.get_children(node)
    descendant_counts = list(map(get_files_count, children))
    return sum(descendant_counts)

def get_subdirectories_info(node):
    children = fs.get_children(node)
    # Нас интересуют только директории
    filtered = filter(fs.is_directory, children)
    # Запускаем подсчет для каждой директории
    # x = lambda child: (fs.get_name(child), get_files_count(child))
    # print(x)
    result = map(
        lambda child: (fs.get_name(child), get_files_count(child)),
        filtered,
    )
    return list(result)

print(get_subdirectories_info(tree))
# => [('etc', 1), ('consul', 2)]

####################3
# items = [2, [3, [4, [5, [6]]], [7]]]

# def agregate(items):
#     if isinstance(items, int):
#         return items
#     result = list(map(
# agregate
# , items))
#     return sum(result)

# print(agregate(items))
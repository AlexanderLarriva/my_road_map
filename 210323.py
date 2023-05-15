import os
from hexlet.fs import flatten, get_children, get_name, is_file
from hexlet.fs import mkdir, mkfile, is_directory


# path1 = "/home/user"
# path2 = "documents"
# filename = "example.txt"

# # Joining the paths
# full_path = os.path.join(path1, path2, filename)

# print(full_path)

def find_files_by_name(tree, substring):
    result = []
    def inner(node, ancestry):
        path = os.path.join(ancestry, get_name(node))
        if is_file(node):
            if substring in get_name(node):
                result.append(path)
        else:
            for child in get_children(node):
                inner(child, path)
    inner(tree, '')
    return result
    
    
    # result = []
    # ancestry = get_name(tree)
    # def inner(subtree, substring):
        
    #     for node in subtree:
    #         if is_directory(node):
    #             ancestry = os.path.join(ancestry, get_name(node))
    #             find_files_by_name(subtree, substring)
    #         else:
    #             if substring in get_name(node):
                    
                
        
    #     return flatten(output)

    # return inner(tree, substring)

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkfile('data'),
            mkfile('raft'),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])


print(find_files_by_name(tree, 'co'))
# ['/etc/nginx/nginx.conf', '/etc/consul/config.json']

with open('example.txt', 'r') as f:
    print(f'tell() before read: {f.tell()}')
    line = f.readline()
    print(f'readline(): {line}')
    print(f'tell() after read: {f.tell()}')
    f.seek(0,2)
    # print(f.readline())
    print(f'tell() after seek(0, 2): {f.tell()}')

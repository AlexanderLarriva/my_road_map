
KEY_LEN = 5
VALUE_LEN = 5

# db = open('./nosql.db', 'w')
# path = db.name  # ./nosql.db

path = './nosql.db'

def set_(path, key, value):
    with open(path, 'r+') as f:
        f.seek(0)
        lines = f.readlines()
        pos = None
        # если файл не пустой, то проводится поиск существующего ключа
        if len(lines) != 0:
            for line in lines:
                k, v = line.strip().split('\t')
                # print(k, v)
                if k == key:
                # здесь должна быть логика перезаписи значения по ключу
                # какой-то глюк с позицией
                    print(f.tell())
                    pos = f.tell() - len(v)
                    print(pos)
                    f.seek(pos)
                    f.write(f"{value}\n")
                    break
            else:
                f.write(f"{key}\t {value}\n")
        # если файл пустой, то записывается строка ключ\значение
        else:
            f.write(f"{key}\t {value}\n")
            
# def set_(path, key, value):
#     with open(path, 'r+') as f:
#         # перемещаем указатель в начало файла
#         f.seek(0)
#         # считываем все строки из файла
#         lines = f.readlines()
#         # ищем строку с ключом
#         for i, line in enumerate(lines):
#             print(i, line)
#             k, v = line.strip().split('\t')
#             if k == key:
#                 # если ключ найден, перезаписываем значение и записываем все строки обратно в файл
#                 f.seek(i * (KEY_LEN + VALUE_LEN), 0)  # перемещаем указатель на нужную позицию
#                 f.write(key.ljust(KEY_LEN) + value.ljust(VALUE_LEN) + '\n')  # записываем строку в файл
#                 return
#         # если ключ не найден, записываем новую строку в файл
#         f.write(key.ljust(KEY_LEN) + value.ljust(VALUE_LEN) + '\n')


set_(path, 'wur', '15')     
        
        
        # f.write("Pos-" + str(f.tell()) + "\n")
        # f.seek(0)
        # lines = f.readlines()
        # f.seek(0, 2)  # перемещаем указатель в конец файла
        # print(lines)
        # print(f.tell())


    # with open(path, 'w') as f:
        # for line in lines:
        #     k, v = line.strip().split('\t')
        #     print(k, v)
        #     if k == key:
        #         f.write(f"{key}\t{value}\n")
        #         break
        #     else:
        #         f.write(line)
        # else:
        #     f.write(f"{key}\t{value}\n")
        
        # for i in file.readlines():
        #     print(i)
            # if key in i:
            #     file.write('Проверка')
            # else:
            #     file.write(f'{key}   {value}')
        # print(file.tell())
    




# def get_(path, key):
    
#     return 1



# get_(path, 'key1')  # 'value1'
# set_(path, 'key1', 'value2')
# get_(path, 'key1')  # 'value2'

# file = open('111.txt', 'a+', encoding='utf-8')
# # print(file.read(5))
# # print(file.read(8))
# # file.seek(0)
# # print(file.read(5))
# # print(file.readline(), end='')
# # file.seek(0)
# # s = file.readlines()
# # print(s)
# # file.seek(0, 2)
# file.write('11')
# print(file.tell())

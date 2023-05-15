db = open('./nosql.db', 'w')
path = db.name  # ./nosql.db
# print(path)

KEY_LEN = 10
VALUE_LEN = 100

def get_(path, key):
    with open(path, 'r') as f:
        while True:
            pos = f.tell()
            line = f.readline()
            if not line:
                return None
            k, v = line[:KEY_LEN], line[KEY_LEN:]
            if k == key:
                return v.strip()

def set_(path, key, value):
    with open(path, 'r+') as f:
        while True:
            pos = f.tell()
            line = f.readline()
            if not line:
                # we've reached the end of the file, so add a new entry
                f.write(key.ljust(KEY_LEN) + value.ljust(VALUE_LEN) + '\n')
                return
            k, v = line[:KEY_LEN], line[KEY_LEN:]
            if k == key:
                # overwrite the existing entry
                f.seek(pos)
                f.write(key.ljust(KEY_LEN) + value.ljust(VALUE_LEN) + '\n')
                return


# import os

# KEY_LEN = 10
# VALUE_LEN = 20

# def set_(path, key, value):
#     with open(path, 'r+') as f:
#         while True:
#             pos = f.tell()
#             line = f.readline()
#             if not line:
#                 break
#             if line[:KEY_LEN] == key:
#                 f.seek(pos)
#                 f.write(value.ljust(VALUE_LEN))
#                 return
#         f.write(key.ljust(KEY_LEN) + value.ljust(VALUE_LEN))

# def get_(path, key):
#     with open(path, 'r') as f:
#         while True:
#             line = f.readline()
#             if not line:
#                 return None
#             if line[:KEY_LEN] == key:
#                 return line[KEY_LEN:KEY_LEN+VALUE_LEN].strip()


set_(path, 'key1', 'value1')
print(get_(path, 'key1'))  # 'value1'
set_(path, 'key1', 'value2')
# get_(path, 'key1')  # 'value2'
set_(path, 'key2', 'value3')
set_(path, 'key24444444444444', 'value4')
set_(path, 'sddddddddddddddddddddddd', 'value3')
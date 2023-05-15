from get_key import get


if get({"hello": "world"}, "hello") != 'world':
    raise Exception('Функция работает неверно!')

if get({}, "hello", "kitty") != "kitty":
    raise Exception('Функция работает неверно!')

if get({"hello": "world"}, "hello", "kitty") != 'world':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
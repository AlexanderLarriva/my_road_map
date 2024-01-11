# Реализуйте функцию length_of_last_word(), которая возвращает длину последнего слова переданной на вход строки. 
# Словом считается любая последовательность не содержащая пробелы, символы перевода строки \n и табуляции \t.


def length_of_last_word(Mystring):
    if not Mystring or Mystring.isspace():
        return 0

    string_to_list = Mystring.split()
    return len(string_to_list[-1])


print(length_of_last_word('hello\t\nworld'))

# length_of_last_word('') == 0
# length_of_last_word(' \t\n') == 0
# length_of_last_word('hi') == 2
# length_of_last_word('Hexlet, hi') == 2
# length_of_last_word('  cat') == 3
# length_of_last_word('man in black') == 5
# length_of_last_word('hello, world!') == 6
# length_of_last_word('hello, wOrLd!    ') == 6
# length_of_last_word('hello\t\nworld') == 5
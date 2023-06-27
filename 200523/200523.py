def letter_multiply(text: str, target_symb: str, num: int) -> str:
    result = ""
    for letter in text:
        if letter != target_symb:
            result += letter
        else:
            result += (letter * num)
    return result
            
text = 'python'
print(letter_multiply(text, 'p', 2)) # => ppython
print(letter_multiply(text, 'y', 3)) # => pyyython
print(letter_multiply(text, 'n', 4)) # => pythonnnn

####################################################
def count_items(count):
    # Объявляем переменную
    result = ''

    # Заполняем
    match count:
        case 1:
            result = 'one'
        case 2:
            result = 'two'
        case _:
            result = None

    # Возвращаем
    return result

print(count_items(2))

######################################

def match_input(input):
    match input:
        case 'start' | 'begin':
            print('Starting...')
        case 'stop' | 'end':
            print('Stopping...')
        case 'pause':
            print('Pausing...')
        case _:
            print('Invalid input')

match_input('begin')  # => Starting...
match_input('stop')  # => Stopping...
match_input('pause')  # => Pausing...
match_input('test')  # => Invalid input

######################################

def get_type(input):
    match input:
        case str(value):
            print(f'It is a string: {value}')
        case int(value):
            print(f'It is an integer: {value}')
        case _:
            print('I dont know this type')

get_type('hello')  # => It is a string: hello
get_type(123)  # => It is an integer: 123
get_type(True)  # => I dont know this type
##################################################

def get_number_explanation(num):
    match num:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'            
        case 7:
            return 'prime number'
        case _:
            return 'just a number'




print(get_number_explanation(77))  # just a number
get_number_explanation(666)  # devil number
get_number_explanation(42)  # answer for everything
get_number_explanation(7)  # prime number

######################################3

def is_happy_ticket(ticket_number: str) -> bool:
    length = len(ticket_number)
    halfs_of_ticket = (ticket_number[:(length//2)], ticket_number[length//2:])
    result = []

    for half in halfs_of_ticket:
        count = 0
        for str_digit in half:
            count += int(str_digit)
        result.append(count)

    if result[0] == result[1]:
        return True
    return False

print(is_happy_ticket('160006')) # True
is_happy_ticket('341800') # True

is_happy_ticket('42') # False
is_happy_ticket('12345678') # False
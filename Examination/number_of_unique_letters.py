# def number_of_unique_letters(Mystring):
#     return len({char: pos for pos, char in enumerate(Mystring.lower()) if char.isalpha()})
    
def number_of_unique_letters(text):
    return len({char.lower() for char in text if char.isalpha()})


# a = "AsDfE"
# print(a.lower())



print(number_of_unique_letters(""))  # 0
print(number_of_unique_letters("abc"))  # 3
print(number_of_unique_letters("A-a-a-a-a-a!"))  # 1
print(number_of_unique_letters("\\(O_o)/"))  # 1
print(number_of_unique_letters("AaBbCcDd"))  # 4
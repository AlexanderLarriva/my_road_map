def enlarge(image: list) -> list: 
    
    result = []
    Mystr = ''
    # if image == []:
    #     return image
    # if image == ['']:
    #     return ['', '']
    for line in image:  # frame = [' 1', '2 ',]
        for char in line:
            Mystr += char*2
        result.append(Mystr)
        result.append(Mystr)
        Mystr = ''
    return result
    
def enlarge1(image: list) -> list:
    if not image:
        return image

    enlarged = [line * 2 for line in image for _ in range(2)]
    return enlarged


def enlarge3(image: list) -> list:
    result = []
    
    for line in image:
        doubled_line = ''
        for char in line:
            doubled_line += char * 2
        result.append(doubled_line)
        result.append(doubled_line)

    return result


        
        
        
        
        #     Mystr = char*2
        #     result.append(Mystr)
        #     result.append(Mystr)
        # return result





def show(image):
    for line in image:
        print(line)
 
dot = ['@']
# show(enlarge(dot))
# => @@
# => @@
# frame = [
#     '****',
#     '*  *',
#     '*  *',
#     '****'
# ]
# frame = ['****', '* *']
# frame = ['12', '34']
frame = ['']
# show(frame)

print(enlarge(frame))
# => ****
# => *  *
# => *  *
# => ****
# show(enlarge(frame))
# => ********
# => ********
# => **    **
# => **    **
# => **    **
# => **    **
# => ********
# => ********
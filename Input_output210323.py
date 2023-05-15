# f = open('foo.txt', 'w')
# print(f)  # <_io.TextIOWrapper name='foo.txt' mode='w' encoding='UTF-8'>
# f.write('Hello\nWorld!')  # 12
# # f.close()
# f = open('foo.txt', 'r')
# print(f.read())
# f.close()
# print(f.closed)
# f.close()
# print(f.closed)

#######################
with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        for i, line in enumerate(input_file, 1):
            output_file.write(
                f"{i}) {line}"
            )
def read_and_rewrite(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    with open(output_file, 'w') as file:
        file.write(content)

# Пример использования
input_file = 'transform/input.txt'
output_file = 'transform/output.txt'

read_and_rewrite(input_file, output_file)

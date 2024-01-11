def word_len_filter(content, min_length):
    words = content.split()
    filtered_words = [word for word in words if len(word) >= min_length]
    
    for i, word in enumerate(filtered_words):
        if word[-1] in [',', '!', '.', '?']:
            filtered_words[i] = word[:-1]
    
    filtered_words = ' '.join(filtered_words)
    return filtered_words


def censored_words(content, censored_words):
    words = content.split()
    for item in censored_words:
        if item in words:
            words.remove(item)
    filtered_words = ' '.join(words)
    return filtered_words

      
def capitalize_letter(content, capital_letters):
    words = content.split()
    for i in range(len(words)):
        word = words[i]
        if word[0] in capital_letters:
            words[i] = word.capitalize()
    capitalized_content = ' '.join(words)
    return capitalized_content


def transform(input_file, output_file, rules):
    with open(input_file, 'r') as file:
        with open(output_file, 'w') as output:
            for line in file:
                line = word_len_filter(line, rules["word_min_len"])
                line = censored_words(line, rules["censored_words"])
                line = capitalize_letter(line, rules["capital_letters"])
                if line.strip():
                    output.write(line + '\n')



# rules = {'capital_letters': ['t', 'c'], 'censored_words': ['better', 'is'], 'word_min_len': 3}

rules = {'capital_letters': ['s', 'p'], 'censored_words': ['explain', 'implementation'], 'word_min_len': 4}
 
print(transform('/home/larriva/MyTraning/transform/input.txt', '/home/larriva/MyTraning/transform/output.txt', rules=rules))

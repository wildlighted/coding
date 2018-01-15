def get_text(filename):
    ''' read file and return the text '''
    with open(filename, encoding='utf-8') as file_object:
        text = file_object.read()
        return text

def tokenize(text):
    ''' tokenize the text '''
    words = text.split()
    return words

def extract_constr(words):
    ''' find np '''
    constr_list = []
    for i,token in enumerate(words):
        splitted = token.split('_')
        # if len(splitted) == 2:
            # word = splitted[0]
            # pos = splitted[1]
        word, pos = '_'.join(splitted[:-1]), splitted[-1]
        if pos == 'A':
            next_word = words[i+1]
            if next_word.endswith('_S'):
                constr_list.append(word + ' ' + next_word[:-2])
    return constr_list

def write_results(constr_list, fname):
    with open(fname, 'w') as f:
        for constr in constr_list:
            f.write(constr + '\n')

def main():
    # pipeline
    raw_text = get_text('sample_tagged_text.txt')
    # print(raw_text[:100])
    tokens = tokenize(raw_text)
    # sprint(tokens[:20])
    constr_list = extract_constr(tokens)
    for entry in constr_list:
        print(entry)
    write_results(constr_list, 'constr.txt')

main()
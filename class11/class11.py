def read_data(fname):
    with open(fname, encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def char_speech(raw_lines):
    char_all_speech = {}
    for line in raw_lines[1:]:
        splitted = line.split(',')
        if len(splitted) > 3:
            name = splitted[2]
            text = ','.join(splitted[3:])
            text = text[1:]
            if name in char_all_speech:
                char_all_speech[name] = char_all_speech[name] + '\n' + text
            else:
                char_all_speech[name] = text
    return char_all_speech

def freq_d(person, char_speech):
    top_words = []
    freq_dict = {}
    no_punct = char_speech.replace('.', ' ')
    no_punct = no_punct.replace(',', ' ')
    tokens = no_punct.split()

    return top_words

def main():
    raw_data = read_data('all-seasons.csv')
    all_speech = char_speech(raw_data)
    #for char in all_speech:
        #print(char, len(all_speech[char]))
    speech_len = {}
    for char in all_speech:
        if char not in speech_len:
            speech_len[char] = len(all_speech[char])
    main_chars_pre = speech_len.items()
    main_chars = []
    for name, length in main_chars_pre:
        main_chars.append([length, name])
    main_chars = sorted(main_chars, reverse=True)[:10]
    main_names = []
    for length, name in main_chars:
        main_names.append(name)
    print(main_names)
    for char in main_names:
        top = freq_d(char, all_speech[char])
        print(char)
        print(top)


if __name__ == '__main__':
    main()


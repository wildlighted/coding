#вариант 2

import re

def read_file(fname):
    with open(fname, encoding="utf-8") as f:
        data = f.read().lower()
    return data

def task_1(text):
    lines = text.split(\n)
    return len(lines)

def task_2(text):
    dict = {}
    keys = []
    wordlines = re.findall("<w lemma=.+</w>", text)
    for wordline in wordlines:
        type = re.search('(?<=type=")[a-z]+(?=")', wordline).group()
        if type not in keys:
            entries = re.findall(type, text)
            dict[type] = len(entries)
            keys = list(dict.keys())
    '\n'.join(keys)
    return keys

def task_3(text):
    adjdict = {}
    keys = []
    wordlines = re.search("<w.+</w>", text).group()
    types = re.findall('(?<=type=")l.f.*(?=")', wordlines)
    for type in types:
        if type not in keys:
            entries = re.findall(type, text)
            adjdict[type] = len(entries)
            keys = list(adjdict.keys())
    return adjdict

def cleartags(text):
    text = re.search('<div1>.+</div1>', flags='re.DOTALL').group()
    text = re.sub('<\w+>', "", text)
    text = re.sub('</\w+>', "", text)
    text = re.sub('<\w >', "", text)
    text = re.sub('>', "", text)

def task_final(cleartext):
    lemmas = re.findall('?<=lemma=")\w+(?=")')
    types = re.findall('(?<=type=")\w+(?=")')
    forms = re.findall('(?<=")\w+(?=\n)')
    outputs = []
    for i in range(len(lemmas)):
        output = ','.join(lemmas[i], types[i], forms[i])
        outputs.append(output)
    return outputs


def write_results(something, fname):
    with open(fname, "w", encoding="utf-8") as f:
        f.write(something)

def main():
    info = read_file('iscorpora.xml')
    write_results('Задание 1\n' + task_1(info) + '\n' + 'Задание 2\n' + task_2(info), 'test_output.txt')
    adjectives = task_3(info)
    adjkeys = list(adjectives.keys())
    result = ""
    for key in adjkeys:
        result = result + key + ' ' + adjectives[key] + '\n'
    write_results(result, 'adjectives.txt')
    info = read_file('iscorpora.csv')
    clear_info = cleartags(info)
    results = task_final(info)
    output = ""
    for line in results:
        output = output + line + '\n'
    write_results(output, 'final.txt')


if __name__ == "__main__":
    main()




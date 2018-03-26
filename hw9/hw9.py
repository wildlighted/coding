# вариант 4
import re

def read_file(fname):
    with open(fname, encoding='utf-8') as f:
        data = f.read().lower()
        data = data.replace('\n', ' ')
        data = data.replace('\t', ' ')
        # print(data)
    return data

def search_verb(text):
    future = re.findall('["\s]?выпь[а-я]*[.,!?:;"\s]*', text)
    past = re.findall('["\s]?выпил[а-я]*[.,!?:;"\s]*', text)
    imper = re.findall('["\s]?выпей[а-я]*[.,!?:;"\s]*', text)
    passparticiples = re.findall('["\s]?выпит[а-я]*[.,!?:;"\s]*', text)
    actparticiples = re.findall('["\s]?выпив(?:ш[а-я]*)?[.,!?:;"\s]*', text)
    results = future + past + imper + actparticiples + passparticiples
    return results

def remove_repetition(res):
    list = []
    for word in res:
        word = word.strip()
        word = word.strip(',.?!:;"')
        if word not in list:
            list.append(word)
    return list

def main():
    text = read_file('text.txt')
    searchresults = search_verb(text)
    forms = remove_repetition(searchresults)
    if forms:
        for form in forms:
            print(form)
    else:
        print('Форм глагола "выпить" в тексте не нашлось :(')

if __name__ == '__main__':
    main()







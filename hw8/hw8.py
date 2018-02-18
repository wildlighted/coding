# вариант 4
import random

def read_data(fname):
    with open(fname, encoding='utf-8') as f:
        raw_data = f.read()
    data = raw_data.split('\n')
    return data

def create_dict(lines):
    dict = {}
    for line in lines:
        clue, word = line.split(',')
        dict[word] = clue
    return dict

def main():
    text = read_data('clues.csv')
    clues = create_dict(text)
    words = list(clues.keys())
    word = random.choice(words)
    clue = clues[word]
    dots = ''
    for i in range(len(clue)):
        dots += '.'
    print('Угадайте слово по подсказке:', clue, dots)
    answer = input('Введите вашу догадку: ').lower()
    if answer == word:
        print('Да, все так.')
    else:
        print('Увы, нет. Ответ - ' + word + '.')

if __name__ == '__main__':
    main()







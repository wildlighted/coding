# вариант 4
inf = []
word = input('Введите латинское слово: ')
if word == '':
    print('Вы ничего не ввели.')
else:
    while word != '':
        if word.endswith('are') or word.endswith('ere') or word.endswith('ire') or word.endswith('ari') or word.endswith('eri') or word.endswith('iri'):
            inf.append(word + '\n')
        word = input()
with open('text.txt', 'w', encoding='utf-8') as f:
    f.writelines(inf)

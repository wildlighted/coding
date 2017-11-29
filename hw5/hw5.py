# вариант 4
inf = []
word = input('Введите латинское слово: ')
if word == '':
    print('Вы ничего не ввели.')
else:
    while word != '':
        # вариант на случай, если предполагается, что пользователь может вводить рандомные сочетания латинских букв:
        # if word.endswith('are') or word.endswith('ere') or word.endswith('ire') 
        # or word.endswith('ari') or word.endswith('eri') or word.endswith('iri'):
        # вариант на случай, если пользователь может вводить только реальные латинские слова:
        if word.endswith('re') or word.endswith('ri'):
            inf.append(word + '\n')
        word = input()
with open('text.txt', 'w', encoding='utf-8') as f:
    f.writelines(inf)

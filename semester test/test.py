with open ('Ozhegov.txt', encoding='utf-8') as f:
    # чтение из файла
    text = f.read()
    lines = text.split('\n')
    #print(lines[:5])
words = []
antonyms = 0
for line in lines:
    columns = line.split('|')
    # задание 1
    if len(columns[0]) >= 20:
        words.append(columns[0])
    # задание 2
    for i,column in enumerate(columns):
        if column == '':
            columns.pop(i)
    if len(columns) > 3:
        #print(columns[0], columns[-2])
        antonyms += 1
if words:
    print('Слова, состоящие не менее чем из 20 символов:\n')
    for word in words:
        print(word+'\n')
print('Количество слов, к которым даны антонимы:', antonyms, '\n')

# задание 3
keyword = input('Введите слово: ')
if keyword == '':
    print('Вы ввели пустую строку. Попробуйте еще разок.')
else:
    while keyword != '':
        k = 0
        for line in lines:
            columns = line.split('|')
            if columns[0] == keyword:
                for i, column in enumerate(columns):
                    if column == '':
                        columns.pop(i)
                print(keyword, '—', columns[-1], '—', columns[1], '\n')
                k = 1
                break
        if k == 0:
            print('Слово не найдено.')
        keyword = input('Введите слово: ')




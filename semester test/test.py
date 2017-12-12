with open ('Ozhegov.txt', encoding='utf-8') as f:
    # чтение из файла
    text = f.read()
    lines = text.split('\n')
    #print(lines[:5])
words = []
antonyms = 0
for line in lines:
    columns = line.split('|') # разбиение строки на колонки по разделителю
    # задание 1
    if len(columns[0]) >= 20:
        words.append(columns[0]) # список слов из как минимум 20 символов
    # задание 2
    for i,column in enumerate(columns):
        if column == '':
            columns.pop(i) #удаление пустых колонок, появившихся из-за двойного разделителя ||
    if len(columns) > 3:
        #print(columns[0], columns[-2])
        antonyms += 1 #подсчет количества антонимов
if words:
    print('Слова, состоящие не менее чем из 20 символов:\n')
    for word in words:
        print(word+'\n')
print('Количество слов, к которым даны антонимы:', antonyms, '\n')

# задание 3
keyword = input('Введите слово: ')
if keyword == '':
    print('Вы ввели пустую строку. Попробуйте еще разок запустить программу.') # проверка первого ввода на пустое слово, чтобы не падало все
else:
    while keyword != '':
        mark = False # сигнал нахождения слова
        for line in lines:
            columns = line.split('|')
            if columns[0] == keyword:
                for i, column in enumerate(columns):
                    if column == '':
                        columns.pop(i)
            # все то же самое разбиение на колонки и удаление пустых
                print(keyword, '—', columns[-1], '—', columns[1], '\n')
                mark = True # отметка нахождения слова
                break
        if not mark:
            print('Слово не найдено.\n')
        keyword = input('Введите следующее слово: ')

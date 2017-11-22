with open('text.txt', encoding='utf-8') as f:
    text = f.readlines()
k = 0
lentext = 0
if not text:
    answer = 'Упс, файл пуст.'
else:
    for line in text:
        line = line.strip('\n')
        if line:
            words = line.split()
            if words:
                lentext += len(words)
                for word in words:
                    if not word.endswith('.') and not word.endswith(','):
                        k += 1
                percentage = k / lentext * 100
                answer = 'В этом файле ' + str(percentage) + '% слов не оканчиваются точкой или запятой.'
            else:
                answer = 'Упс, в файле только пробелы или переносы строки.'
        else:
            answer = 'Упс, в файле только пробелы или переносы строки.'
print(answer)

#вариант 4

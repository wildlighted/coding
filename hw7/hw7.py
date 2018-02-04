# вариант 4
def openfile(): # функция открывает файл с именем, которое пользователь ввел с клавиатуры, проверяет его правильность, в случае удачи возвращает текст из него
    fname = input('Enter file name: ')
    if not fname.endswith('.txt'):
        print('Your file name is not valid :(')
        text = ''
    else:
        with open(fname, encoding='utf-8') as f:
            text = f.read()
    return text

def formcount(list): # функция подсчитывает количество вхождений на -ed и -ied в разделенном на "слова" тексте, возвращает список из этих двух значений в соответствующем порядке
    count_ed = 0
    count_ied = 0
    for element in list:
        if element.endswith('ed'):
            count_ed += 1
            if element.endswith('ied'):
                count_ied += 1
    count = [count_ed, count_ied]
    return count

def main(): #функция проверяет текст на пустоту, в случае удачи делит текст из открытого файла на "слова" по пробелам, считает количество нужных форм, выводит оба значения
    englishtext = openfile()
    if not englishtext:
        print('There is nothing in your text :(')
    else:
        words = englishtext.split()
        answer = formcount(words)
        print(answer[0], 'forms in text end with "-ed"')
        print('Out of those,', answer[1], 'forms end with "-ied"')

if __name__ == '__main__':
    main()

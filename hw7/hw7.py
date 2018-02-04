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

def formcount(elements): # функция подсчитывает количество форм на -ed и -ied в разделенном на "слова" без знаков препинания тексте, возвращает список из этих двух значений в соответствующем порядке
    count_ed = 0
    count_ied = 0
    for element in elements:
        clear = element.strip('!?-:;.,')
        if clear.endswith('ed'):
            count_ed += 1
            if clear.endswith('ied'):
                count_ied += 1
    count = [count_ed, count_ied]
    return count

def main(): #функция проверяет текст на пустоту, в случае удачи делит текст из открытого файла на "слова" по пробелам, считает количество нужных форм, выводит оба значения
    englishtext = openfile()
    if not englishtext:
        print('There is nothing to count :(')
    else:
        words = englishtext.split()
        answer = formcount(words)
        print(answer[0], 'forms in text end with "-ed" (probably 2nd and 3rd forms of the verbs)')
        print('Out of those,', answer[1], 'forms end with "-ied" (probably derived from verbs ending with -y or -ie)')

if __name__ == '__main__':
    main()

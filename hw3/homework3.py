# Вариант 4
x = int(input('Введите число:'))
if x > 0:
    for i in range(x):
        word = input('Введите слово:')
        if word == 'Программирование' or word == 'программирование':
            break
        else:
            print(word)
else:
    x = int(input('Введите положительное число:'))
    for i in range(x):
        word = input('Введите слово:')
        if word == 'Программирование' or word == 'программирование':
            break
        else:
            print(word)
print('Конец')

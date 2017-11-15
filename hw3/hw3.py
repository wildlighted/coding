#Вариант 4
word = input('Введите слово: ')
if word == '':
    print('Ну, видимо, вы не хотите ничего вводить. Что тут поделаешь.')
else:
    for i in range(len(word)):
        print(word)
        word = word[-1] + word[:-1]
        
    

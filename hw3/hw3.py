#Вариант 4
word = input('Введите слово: ')
if word == '':
   word = input('Нет, введите непустую строку в качестве слова: ')
if word != '':
    for i in range(len(word)):
        print(word)
        word = word[-1] + word[:-1]
else:
    print('Ну, видимо, вы не хотите ничего вводить. Что тут поделаешь.')
  
        
    

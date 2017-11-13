#Вариант 4
word = input('Введите слово: ')
for i in range(len(word)):
    print(word)
    word = word[-1] + word[:-1]
vowels = set('аеиоуыэюя')
line = input('Введите фразу на русском: ')
words = line.split(' ')
brick = ''
for word in words:
    k = 0
    bword = word
    for letter in word:
        k += 1
        if letter in vowels:
            bword = bword[:k] + 'с' + letter + bword[k:]
            k += 2
    brick = brick + ' ' + bword
print(brick)


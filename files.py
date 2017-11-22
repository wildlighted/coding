with open('text.txt', encoding='utf-8') as f:
    text = f.readlines()
k = 0
lentext = 0
for line in text:
    line = line.strip('\n')
    words = line.split()
    lentext += len(words)
    for word in words:
        if not word.endswith('.') and not word.endswith(','):
            k += 1
percentage = k/lentext*100
answer = 'В этом файле ' + str(percentage) + '% слов не оканчиваются точкой или запятой.'
print(answer)
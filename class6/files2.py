filename = 'text.txt'
sent = 'the feeling that the world is collapsing in on itself and we are powerless to stop it'
lines = []
words = sent.split()
#for i in range(len(words)):
for i,w in enumerate(words):
    if i % 2 != 0:
        lines.append(str(i)+' '+w.upper()+'\n')
    else:
        lines.append(str(i)+' '+w+'\n')
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

# mode 'w' - write, 'a' - append, 'r' - read
# можно вместо индексов сделать булеан и менять его каждый раз!!
'''with open (filename, 'w', encoding='utf-8') as f:
    for i,w in enumerate(words):
        print(i,w)
        if i%2 != 0:
            f.writelines(str(i) + ' ' + w.upper())
        else:
            f.writelines(str(i) + ' ' + w)
'''



# файл понимает ток строки, все числа надо переводить
# fname = 'C:\Users\user\Desktop\new 1.txt'
#чтобы не было косяков: префикс r для норм восприятия слэшей или двойной обратный слэш
fname = r'C:\Users\user\Desktop\new 1.txt'
# \n - new line; \t - tabulation
with open(fname, encoding='utf-8') as f:
    text = f.read()
    lines = f.readlines()
    #readlines сразу создает список с элементами-строками файла
  #  print(type(f))
  #  print(type(text))
# type - тип переменной
# текст записывается в f, переводится в строку в t
# ИЛИ ТАК:
'''
text = ''
f = open(fname)
text = f.read()
print(text)
f.close
print(text[:280])
'''
# '\t oh fuck \n \t\t'.strip #strip снимает все эти допсимволы оставляет ток текст
print('\t oh fuck \n \t\t'.strip)
# 'oh god'.isupper() - true если в верхнем регистре вся строка false если нет
# islower аналогично для нижнего
textlist = []
lines = text.split('\n')
# print(lines[:3])
for line in lines:
    words = line.split()
    textlist.append(words)
    for word in words:
        print(word)
    print()
print(textlist)






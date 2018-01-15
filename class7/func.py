'''def hello(user1):
    # понятно шо задать я могу сколько угодно аргументов и таких типов которые мне нужны
    # и их порядок важен
    m = user1.title()
    return m #возвращать можем что угодно; это и будет тип выходных данных ф-ции
heh = hello('mda')
print(heh)
# локальные и глобальные переменные я могу разлиить ток по именам, вестимо'''

def letters(word): # будет в данном случае работать со списком понятно почему
    for sym in word:
        print(sym)
    print(len(word))

#letters('prisms')


def tokenise(line):
    words = line.split()
    return words


def tolines(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
    clear_lines = []
    for line in lines:
        clear_line = line.strip()
        if clear_line:
            clear_lines.append(clear_line)
    return clear_lines

lines_text = tolines('text.txt')
#print(lines_text)

def shortest(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
    short = 10000
    for line in lines:
        short = min(short, len(line))
    return short

print(shortest('text.txt'))




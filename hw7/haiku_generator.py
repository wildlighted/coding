#вариант 4
import random

def tokenizefile(fname):
    tokens = []
    with open (fname, encoding='utf-8') as f:
        text = f.read()
        tokens = text.split('\n')
    return tokens

def verbs_1():
    verbs_1 = tokenizefile('verbs_1.txt')
    return random.choice(verbs_1)

def verbs_2():
    verbs_2 = tokenizefile('verbs_2.txt')
    return random.choice(verbs_2)

def nouns_1():
    nouns_1 = tokenizefile('nouns_1.txt')
    return random.choice(nouns_1)

def nouns_2():
    nouns_2 = tokenizefile('nouns_2.txt')
    return random.choice(nouns_2)

def adjectives():
    adjectives = tokenizefile('adjectives.txt')
    return random.choice(adjectives)

def links():
    links = tokenizefile('links.txt')
    return random.choice(links)

def punct():
    punct = tokenizefile('punct.txt')
    return random.choice(punct)

def main():
    for i in range(0,3):
        if i % 2 == 0:
            variant = random.randint(1, 2)
            if variant == 1:
                print(verbs_1() + ' ' + 'die' + ' ' + nouns_1() + punct())
            else:
                verb_2 = verbs_2()
                verb = verb_2.split(' ')
                print(verb[0] + ' ' + nouns_2() + ' ' + verb[1] + punct())
        else:
            print(links() + ', ' + adjectives() + ' ' + nouns_1() + punct())

if __name__ == '__main__':
    main()


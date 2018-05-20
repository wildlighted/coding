#вариант 4
import os

def countnames():
    filenames = os.listdir()
    firstsym = [filename[0].lower() for filename in filenames]
    symcount = {sym: 0 for sym in firstsym}
    for filename in filenames:
        symcount[filename[0].lower()] += 1
    return symcount

def main():
    letters_counted = countnames()
    print(sorted(letters_counted, key=letters_counted.get, reverse=True)[0])

if __name__ == '__main__':
    main()

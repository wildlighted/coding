#вариант 4
import os

def countnames():
    filenames = os.listdir()
    symcount = {}
    for filename in filenames:
        if filename[0].lower() in symcount.keys():
            symcount[filename[0].lower()] += 1
        else:
            symcount[filename[0].lower()] = 1
    return symcount

def main():
    letters_counted = countnames()
    print(sorted(letters_counted, key=letters_counted.get, reverse=True)[0])

if __name__ == '__main__':
    main()

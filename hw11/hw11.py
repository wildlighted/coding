#вариант 4

import re

def read_file():
    with open('Философия.html', encoding="utf-8") as f:
        data = f.read()
    return data

def write_answer(answer):
    with open("Астрология.html", "w", encoding="utf-8") as f:
        f.write(answer)

def substitute(text):
    substituted = re.sub('Филос(о.?)фи(?=[а-я]+)', r'Астрол\1ги', text) #группа для учета символа о с ударением (которое на википедии доп.символ после буквы)
    substituted = re.sub('филос(о.?)фи(?=[а-я]+)', r'Астрол\1ги', text)
    substituted = re.sub('ФИЛОС(О.?)ФИ(?=[А-Я]+)', r'АСТРОЛ\1ГИ', substituted)
    return substituted

def main():
    info = read_file()
    result = substitute(info)
    write_answer(result)

if __name__ == "__main__":
    main()

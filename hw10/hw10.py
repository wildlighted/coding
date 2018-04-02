#вариант 4
import re

def read_file():
    fname = input("Введите название файла без расширения: ")
    with open(fname + '.html', encoding="utf-8") as f:
        data = f.read().lower()
    return data

def find_field(data): #обрезает html код так, что остается только то, что после заголовка "Научная сфера" и до конца параграфа, в котором перечислены сферы
    result = re.search("научная сфера[\S\s]+", data)
    if result:
        field = result.group()
    else:
        field = ''
    return field

def define_field(some_field): #ищет в обрезанном коде все теги параграфов, в первом из них все вхождения кириллического текста внутри тегов ссылок (чтобы избежать повторов из-за заголовков)
    paragraphs = re.findall("<p>.+\s</p>", some_field)
    fields = re.findall(">[а-я]+(?: ?[а-я]*)*<", paragraphs[0])
    return ", ".join(fields).replace(">", "").replace("<", "")

def write_answer(answer):
    with open("answer.txt", "w", encoding="utf-8") as f:
        f.write(answer)

def main():
    text = read_file()
    search_results = find_field(text)
    if search_results:
        science_fields = define_field(search_results)
        write_answer("Сфера работы этой ученой или ученого — " + science_fields + ".")
    else:
        write_answer("Кажется, на этой странице нет информации о научной сфере...")

if __name__ == "__main__":
    main()

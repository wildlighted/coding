#ВАРИАНТ ЧЕТЫРЕ
import re

def read_file():
   fname = input('Введите имя файла: ')
   try:
       with open(fname, encoding='utf-8') as f:
           text = f.read()
       return text
   except FileNotFoundError as error:
       return print('Файла с таким названием не существует. Программа сейчас завершится, попробуйте потом еще разок.') + exit(0)

def clear_text(text):
    sentences = re.split('[.?!]*[!.?]+\n*', text) #делю текст на предложения, учитывая такие варианты, как '?!', '?..' и прочие подобные сочетания на границах и переносы строк
    clear_sentences = [re.sub('[,:;"()—–\xa0]', '', sentence) for sentence in sentences] #чищу от знаков препинания
    return clear_sentences

def generate_len_dict(sentence):
    lens = {word: len(word) for word in sentence.split(' ') if word} #чтобы он не считал пробелы в начале предложений, оставшиеся от разбиения прямой речи
    return lens

def generate_full_dict(sentences):
    dict_full = {sentence: generate_len_dict(sentence) for sentence in sentences}
    return dict_full

def main():
    data = read_file()
    clear_data = clear_text(data)
    dict = generate_full_dict(clear_data)
    print(dict)

if __name__ == "__main__":
    main()







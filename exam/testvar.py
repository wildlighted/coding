import re
import collections
import os

def read_file(fname):
    with open(fname, encoding='windows-1251') as f:
        text = f.read()
    return text

def clear_tag(tag):
    tag = tag.split()[1]
    tag = re.sub('content="', '', tag.strip('"'))

def find_meta():
    articles = os.listdir('news')
    docids = []
    authors = []
    created = []
    topics = []
    tagging = []
    names = []
    for article in articles:
        text = read_file('news/' + article)
        head = text.split('<head>')[1]
        head = head.split('</head>')[0]
        artname = head.split('<title>')[1]
        artname = artname.split('</title>')[0]
        meta = head.split('</title>')[1]
        tags = meta.split('\n')[1:-1]
        clear_tags = []
        for tag in tags:
            tag = tag.split('<meta content="')[1]
            tag = tag.split('" name')[0]
            clear_tags.append(tag)
        docids.append(clear_tags[-1])
        authors.append(clear_tags[1])
        created.append(clear_tags[3])
        topics.append(clear_tags[7])
        tagging.append(clear_tags[0])
        names.append(artname)
    with open('info.csv', 'w', encoding='windows-1251') as f:
        #как выяснилось за 5 минут до конца, я не так поняла описание таблицы, и думала, что имеются в виду горизонтальные поля с информацией для всех статей, разделенной запятыми.
        #но хотя бы такой вывод у меня работает нормально, хоть поправить на нужный формат я не успела
        #еще я не сразу осознала, что не везде теги в одном порядке, так что в графе created где-то смешаны даты и темы, исправление чего через re.search я тоже просто не успела дописать
        f.write('doc_id , ' + ' , '.join(docids) + '\n')
        f.write('title , ' + ' , '.join(names) + '\n')
        f.write('author , ' + ' , '.join(authors) + '\n')
        f.write('created , ' + ' , '.join(created) + '\n')
        f.write('topic , ' + ' , '.join(topics) + '\n')
        f.write('tagging , ' + ' , '.join(tagging) + '\n')

def find_abbreviations():
    articles = os.listdir('news')
    common_text = ''
    abbrs = []
    for article in articles:
        text = read_file('news/' + article)
        common_text = common_text + text
        body = text.split('<body>')[1]
        body = body.split('</body>')[0]
        words = re.findall('<w>.+</w>', body)
        for tag in words:
            tag = tag.split('<w><ana lex="')[1]
            tag = tag.split('" gr')[0]
            if tag.isupper():
                abbrs.append(tag)
    count = {abbr: len(re.findall(abbr, common_text)) for abbr in abbrs}
    with open('abbreviations.csv', 'w', encoding='windows-1251') as f:
        for key, value in count.items():
            f.write(key + '\t' + str(value) + '\n')

def main():
    find_meta()
    find_abbreviations()

if __name__ == "__main__":
    main()

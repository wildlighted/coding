import re
text = 'A.M. Kuchling <amk@amk.ca>'
#text = text.replace('.', '_')
text = text.replace(' ', '_')
#print(text)
emails = 'morse@gmail.com loves @music, someone@somewhere.ru is a user, somewhere.ru is not'
#result = re.sub('[-\w.]+@[-\w.]+\.\w+', '<email>', emails)
#result = re.sub('@[-\w.]+\.\w+', '@hse.ru', emails)
#print(result)
text = "О'Хара; мдауш... по-человечески?!"
#print(re.split("[^\w'-]+", text))
#print(re.findall("\w+[-'\w]?\w+", text))

def check_email():
    user = input('Введите email:\n')
    match_result = re.match("[-\w.]+@[-\w.]+\.\w+", user)
    if match_result:
        print('Окей')
    else:
        print('Ебать вы лох')

#check_email()

def check_number():
    phone = input('Введите номер телефона:\n')
    match_result = re.match("(\+7|8)\d{10}$", phone)
    if match_result:
        print('Окей')
    else:
        print('Ебать вы лох')

#check_number()

def check_vowel():
    word = input('Введите слово:\n')
    word = word.lower()
    match_result = re.match("[аеёиоуыэюя]", word)
    if match_result:
        print('Окей')
    else:
        print('Ебать вы лох')

check_vowel()
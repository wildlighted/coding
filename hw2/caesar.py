code1 = 'abcdefghijklmnopqrstuvwxyz'
code2 = 'bcdefghijklmnopqrstuvwxyza'
word = input('Enter your word:')
caesar = ''
for letter in word:
    for i in range(len(code1)):
        if code1[i] == letter:
            caesar += code2[i]
            break
print(caesar)

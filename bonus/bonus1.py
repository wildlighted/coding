q = 0
s = 0
print('Введите числа:')
while True:
    num = input()
    if num != '':
        q +=1
        s += int(num)
    else:
        break
if q > 0:
    print('Среднее арифметическое введенных чисел равно', s/q)
else:
    print('Вы не ввели ни одного числа.')

q = 0
s = 0
A = set()
print('Введите числа:')
while True:
    num = input()
    if num != '':
        A.add(num)
        q +=1
        s += int(num)
    else:
        break
if q > 0:
    print('Среднее арифметическое введенных чисел равно', s/q)
    list(A)
    print('Максимальное из введенных чисел равно', max(A))
    print('Минимальное из введенных чисел равно', min(A))
else:
    print('Вы не ввели ни одного числа.')
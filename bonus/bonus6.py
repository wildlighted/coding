h = float(input('Введите рост в сантиметрах: ')) / 100
m = float(input('Введите массу тела в килограммах: '))
index = m / (h ** 2)
if index <= 16:
    print('Индекс массы тела равен', index, ': выраженный дефицит массы тела')
elif index > 16 and index <= 18.5:
    print('Индекс массы тела равен', index, ': дефицит массы тела')
elif index > 18.5 and index <= 24.99:
    print('Индекс массы тела равен', index, ': норма')
elif index >= 25 and index <= 30:
    print('Индекс массы тела равен', index, ': избыточная масса тела (предожирение)')
elif index > 30 and index <= 35:
    print('Индекс массы тела равен', index, ': ожирение первой степени')
elif index > 35 and index <= 40:
    print('Индекс массы тела равен', index, ': ожирение второй степени')
elif index > 40:
    print('Индекс массы тела равен', index, ': ожирение третьей степени (морбидное)')



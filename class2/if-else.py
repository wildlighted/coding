year = int(input('Enter year number:'))
#y = int(input('Enter 2nd number:'))

# wl = len(word)
# print(wl)


#if num >0:
  #  print(num, 'больше нуля')
# elif num <= 0:
  #  print(num, 'не больше нуля')
   # if num > -2:
      #  print('огого ничего себе')
    #else:
       # print(num, 'не больше -2')
    # num = num + 100
    # num -= 100
# print(num)

#if num > 0 and num <= 65:
  #  print('Число находится в промежутке от 1 до 65')

# if num > 0 or num <= 65:
   # print('Число положительно или не больше 65')

#if (x % 2) == 0:
  #  print(x, '- чётное число')
#else:
 #   print(x, '- нечётное число')

#if (y % 2) == 0:
#    print(y, '- чётное число')
#else:
#    print(y, '- нечётное число')

# if (x%2) == 0 and (y%2) == 0:
 #   print('Оба числа чётные')
#elif (x%2) == 0 and (y%2) != 0:
#    print ('x - чётное число, а y - нечётное число')
#elif (x%2) != 0 and (y%2) == 0:
#    print ('y - чётное число, а x - нечётное число')
#else:
  #  print('Оба числа нечётные')

# if x > 0:
 #   print(1)
#elif x == 0:
#    print(0)
#else:
 #   print(-1)

if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(year, '- високосный год')
else:
    print(year, '- не високосный год')
    
print('End')

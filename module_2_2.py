print('Введите три произвольных целых числа')
first = int(input('Первое: '))
second = int(input('Второе: '))
third = int(input('Третье: '))
if first == second == third:
    print(3, '- все числа одинаковы.')
elif first == second or second == third or first == third:
    print(2, '- два числа одинаковы.')
else:
    print(0, '- нет одинаковых чисел.')
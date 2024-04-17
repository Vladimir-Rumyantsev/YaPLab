def next_number(string):
    arr = list(string)
    index = 0

    for i in range(len(string)):
        try:
            x = int(arr[index])
            yield x
        except:
            pass
        index += 1


st = input('\nВведите строку: ')
count = 1
line = '\nРезультат: ['

for integer in next_number(st):
    line = f'{line}{integer}, '
    count += 1

if count > 1:
    print(f'{line[:-2]}]')
else:
    print(f'\nВ исходной строке нет цифр')

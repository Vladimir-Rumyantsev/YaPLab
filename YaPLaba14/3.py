class Client:
    def __init__(self, year, month, code, duration):
        self.year = year
        self.month = month
        self.code = code
        self.duration = duration


def binary_insertion_sort(arr, lam=lambda x: x):  # Сортировка массива по какому-то свойству его элементов
    for i in range(1, len(arr)):  # Сортировка бинарными вставками
        key = arr[i]  # Запоминаем элемент с которым работаем сейчас
        left, right = 0, i  # Границы отсортированной части массива
        while left < right:  # Пока левый указатель и правый не на одном элементе
            mid = (left + right) // 2  # Создаём центральный указатель
            if lam(arr[mid]) <= lam(key):  # Сравниваем с ключом элемент на центральном указателе по свойству
                left = mid + 1  # Если ключ больше - сдвигаем левый и центральный указатель вправо
            else:  # Иначе (если ключ меньше центрального указателя), значит нужная ячейка левее
                right = mid  # центрального указателя, значит правому указателю даём значение центрального
        for j in range(i, left, -1):  # Все указатели смотрят на одну ячейку, всё что правее неё сдвигаем
            arr[j] = arr[j - 1]  # на один элемент вправо, чтобы освободить место для ключа
        arr[left] = key  # В освобождённую ячейку записываем значение ключа
    return arr  # Вернуть отсортированный массив


# Считываем входные данные
k = int(input('\nВведите "K" код клиента (в диапазоне 10–99): '))
n = int(input('Введите целое число N (Количество клиентов): '))
print('\nЗаполните базу данных согласно следующей инструкции...\nДля каждого клиента через пробел введите '
      '"<Год> <Номер месяца> <Код клиента> <Продолжительность занятий (в часах)>"\n'
      'Все данные должны быть целочисленными. Значение года должно лежать в диапазоне от 2000 до 2010, '
      'код клиента — в диапазоне 10–99, продолжительность занятий — в диапазоне 1–30\n'
      'Пример того, что программа ожидает увидеть на вход: "2005 6 67 24"')

database = []
for i in range(n):
    try:
        x = list(map(int, input(f'Введите данные для клиента номер {i+1}: ').split()))
        if (2000 <= x[0] <= 2010) and (1 <= x[1] <= 12) and (10 <= x[2] <= 99) and (1 <= x[3] <= 30) and (len(x) == 4):
            database.append(Client(x[0], x[1], x[2], x[3]))
            print('Клиент успешно добавлен в базу данных!\n')
        else:
            print('Кажется вы что-то ввели неправильно, клиент не добавлен!\n')
    except:
        print('Кажется вы что-то ввели неправильно, клиент не добавлен!\n')

client_data = []
for i in range(len(database)):
    if database[i].code == k:
        client_data.append(database[i])

client_data = (binary_insertion_sort
               (binary_insertion_sort
                (binary_insertion_sort
                 (client_data, lambda x: -x.month), lambda x: x.duration), lambda x: x.year))

output = {}
x = 0
for i in client_data:
    if not (i.year in output):
        output[i.year] = i
    elif (output[i.year]).duration > i.duration:
        output[i.year] = i

if not output:
    print('Нет данных!')
else:
    print('Год  | Месяц | Продолжительность занятий в этом месяце')
    for i in output:
        if 1 <= output[i].month <= 9:
            print(f'{output[i].year} | 0{output[i].month}    | {output[i].duration} часов')
        else:
            print(f'{output[i].year} | {output[i].month}    | {output[i].duration} часов')

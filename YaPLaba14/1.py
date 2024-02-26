class FitnessClient:
    def __init__(self, year, month, duration, client_code):
        self.year = year
        self.month = month
        self.duration = duration
        self.client_code = client_code


N = int(input('Введите число N (количество клиентов фитнес-центра): '))
mx_duration = 0
mx = None

print('\nВводите через пробел данные о всех клиентах фитнес-центра в формате "<Год> <Номер месяца> <Продолжительность '
      'занятий (в часах)> <Код клиента>"\nВсе данные — число, значение года лежит в диапазоне от 2000 до 2010, код '
      'клиента — в диапазоне 10–99, продолжительность занятий — в диапазоне 1–30\nПример: 2008 11 24 98\n')

for i in range(N):
    year, month, duration, client_code = map(int, input(f'Введите данные для клиента номер {i+1}: ').split())
    client = FitnessClient(year, month, duration, client_code)

    if not ((2000 <= year <= 2010) and (1 <= month <= 12) and (1 <= duration <= 30) and (10 <= client_code <= 99)):
        print(f'Введённые вами данные для клиента номер {i+1} — некорректны, они не будут учтены')
    elif duration > mx_duration:
        mx_duration = duration
        mx = client

print(mx.duration, mx.year, mx.month)

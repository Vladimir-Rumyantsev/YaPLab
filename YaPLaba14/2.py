file = 'database_2.bin'
database = []


class Student:
    def __init__(self, last_name, first_name, grade):
        self.last_name = last_name
        self.first_name = first_name
        self.grade = grade


class FirstGradeStudent(Student):
    def __init__(self, last_name, first_name, grade, information):
        super().__init__(last_name, first_name, grade)
        self.information = information

    def __str__(self):
        return (f'Имя ученика: {self.last_name}'
                f'\nФамилия ученика: {self.first_name}'
                f'\nКласс ученика: {self.grade}'
                f'\nСкорость чтения: {self.information}')


class SecondOrThirdGradeStudent(Student):
    def __init__(self, last_name, first_name, grade, information):
        super().__init__(last_name, first_name, grade)
        self.information = information

    def __str__(self):
        return (f'Имя ученика: {self.last_name}'
                f'\nФамилия ученика: {self.first_name}'
                f'\nКласс ученика: {self.grade}'
                f'\nДанные итоговой школьной контрольной по математике: {self.information}')


class FourthGradeStudent(Student):
    def __init__(self, last_name, first_name, grade, information):
        super().__init__(last_name, first_name, grade)
        self.information = information

    def __str__(self):
        return (f'Имя ученика: {self.last_name}'
                f'\nФамилия ученика: {self.first_name}'
                f'\nКласс ученика: {self.grade}'
                f'\nБаллы итоговой аттестации: {self.information}')


def student_data(n):
    last_name = input(f'\nВводим данные для ученика номер {n}\nВведите фамилию ученика: ')
    first_name = input('Введите имя ученика: ')
    grade = str(input(f'Введите класс в котором обучается {last_name} {first_name} '
                      f'(в формате <число><буква>, например: "4Г"): '))
    if grade[:-1] == '1':
        try:
            information = int(input(f'Введите скорость чтения для ученика "{last_name} {first_name}" '
                                    f'(число слов в минуту): '))
            database.append(FirstGradeStudent(last_name, first_name, grade, information))
            print(f'Ученик "{last_name} {first_name}" успешно добавлен в базу данных!')
        except:
            print(f'Вы ввели некорректные данные для ученика "{last_name} {first_name}". '
                  f'Его данные не записаны в базу данных!')
    elif grade[:-1] in ['2', '3']:
        try:
            information = float(input(f'Введите данные итоговой школьной контрольной по математике '
                                      f'(оценка от 1 до 10 баллов) для ученика "{last_name} {first_name}": '))
            if float(1) <= information <= float(10):
                database.append(SecondOrThirdGradeStudent(last_name, first_name, grade, information))
                print(f'Ученик "{last_name} {first_name}" успешно добавлен в базу данных!')
            else:
                print(f'Вы ввели некорректные данные для ученика "{last_name} {first_name}". '
                      f'Его данные не записаны в базу данных!')
        except:
            print(f'Вы ввели некорректные данные для ученика "{last_name} {first_name}". '
                  f'Его данные не записаны в базу данных!')
    elif grade[:-1] == '4':
        try:
            information = float(input(f'Введите данные о баллах за итоговую аттестацию (единый муниципальный тест '
                                      f'от 1 до 100 баллов) для ученика "{last_name} {first_name}": '))
            if float(1) <= information <= float(100):
                database.append(FirstGradeStudent(last_name, first_name, grade, information))
                print(f'Ученик "{last_name} {first_name}" успешно добавлен в базу данных!')
            else:
                print(f'Вы ввели некорректные данные для ученика "{last_name} {first_name}". '
                      f'Его данные не записаны в базу данных!')
        except:
            print(f'Вы ввели некорректные данные для ученика "{last_name} {first_name}". '
                  f'Его данные не записаны в базу данных!')
    else:
        print(f'Вы ввели некорректные данные класса для ученика "{last_name} {first_name}". '
              f'Его данные не записаны в базу данных!')


def write_database():
    with open(file, 'wb') as f:
        for i in database:
            str_write = f'{i.last_name} {i.first_name} {i.grade} {i.information}'
            f.write(str_write.encode('utf-8') + b'\n')


def read_database():
    with open(file, 'rb') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line_decode = list((line.decode('utf-8').strip()).split())
            last_name = line_decode[0]
            first_name = line_decode[1]
            grade = line_decode[2]
            if line_decode[2][:-1] == '1':
                information = int(line_decode[3])
                database.append(FirstGradeStudent(last_name, first_name, grade, information))
            elif line_decode[2][:-1] == '4':
                information = float(line_decode[3])
                database.append(FourthGradeStudent(last_name, first_name, grade, information))
            else:
                information = float(line_decode[3])
                database.append(SecondOrThirdGradeStudent(last_name, first_name, grade, information))


N = int(input('\nВведите N (количество учеников): '))
for i in range(N):
    student_data(i+1)
write_database()
database = []
read_database()
for i in range(len(database)):
    print(f'\n{i+1}. {str(database[i])}')

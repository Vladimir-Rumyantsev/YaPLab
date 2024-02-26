# class RoboticMailDelivery:
#     def __init__(self):
#         self.house_flat_pairs = []
#
#     def add_mail(self, house_number, flat_number):
#         '''Добавить информацию о доставке письма по номеру дома
#         house_number, квартире flat_number.'''
#         self.house_flat_pairs.append((house_number, flat_number))
#
#     def flat_numbers_for_house(self, house_number):
#         '''Вернуть список квартир в доме house_number,
#         в которые нужно доставить письма.'''
#         flat_numbers = []
#         for h, f in self.house_flat_pairs:
#             if h == house_number:
#                 flat_numbers.append(f)
#         return flat_numbers
#
#
# class Time:
#     def __init__(self, minutes, seconds):
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def __add__(self, other):
#         m = self.minutes + other.minutes
#         s = self.seconds + other.seconds
#         m += s // 60
#         s = s % 60
#         return Time(m, s)
#
#     def __str__(self):
#         return f'{self.minutes}:{self.seconds}'
#
#
# N = int(input('Введите число N: '))
#
#
#
# class FitnessClient:
#     def __init__(self, year, month, duration, client_code):
#         self.year = year
#         self.month = month
#         self.duration = duration
#         self.client_code = client_code
#
#
# N = int(input('Введите число N (количество клиентов фитнес-центра): '))
# mx_duration = 0
# mx = None
#
# print('\nВводите через пробел данные о всех клиентах фитнес-центра в формате "<Год> <Номер месяца> <Продолжительность '
#       'занятий (в часах)> <Код клиента>"\nВсе данные — число, значение года лежит в диапазоне от 2000 до 2010, код '
#       'клиента — в диапазоне 10–99, продолжительность занятий — в диапазоне 1–30\nПример: 2008 11 24 98\n')
#
# for i in range(N):
#     year, month, duration, client_code = map(int, input(f'Введите данные для клиента номер {i+1}: ').split())
#     client = FitnessClient(year, month, duration, client_code)
#
#     if not ((2000 <= year <= 2010) and (1 <= month <= 12) and (1 <= duration <= 30) and (10 <= client_code <= 99)):
#         print(f'Введённые вами данные для клиента номер {i+1} — некорректны, они не будут учтены')
#     elif duration > mx_duration:
#         mx_duration = duration
#         mx = client
#
# print(mx.duration, mx.year, mx.month)

# from math import pi
#
#
# class Shape:
#     def describe(self):
#         # Атрибут __class__ содержит класс или тип объекта self
#         # Атрибут __name__ содержит строку,
#         # в которой написано название класса или типа
#         print(f"Класс: {self.__class__.__name__}")
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.r = radius
#
#     def area(self):
#         return pi * self.r ** 2
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#
# shape = Shape()
# shape.describe()
#
# circle = Circle(1)
# circle.describe()
#
# rectangle = Rectangle(1, 2)
# rectangle.describe()
#



#
#     with (open(f, 'rb') as file):
#         packed_data = file.read()
#         unpacked_numbers = [int.from_bytes(packed_data[i:i + 4], byteorder='little', signed=True)
#                             for i in range(0, len(packed_data), 4)]
#     return unpacked_numbers
#
#
#
# numbers = []
# n = int(input('\nВведите количество элементов в файле: '))
# print()
# for i in range(n):
#     numbers.append(int(input('Введите новый элемент в файл: ')))
#
#
# with open('input_3.bin', 'wb') as file:
#     for i in numbers:
#         file.write(i.to_bytes(4, byteorder='little', signed=True))
#
#
# # students = []
# # for _ in range(n):
# #     last_name = input("Введите фамилию ученика: ")
# #     first_name = input("Введите имя ученика: ")
# #     grade = int(input("Введите класс ученика: "))
# #
# #     if grade == 1:
# #         reading_speed = int(input("Введите скорость чтения (слов в минуту): "))
# #         student = FirstGradeStudent(last_name, first_name, grade, reading_speed)
# #     elif grade == 2 or grade == 3:
# #         math_score = float(input("Введите оценку по математике: "))
# #         student = SecondOrThirdGradeStudent(last_name, first_name, grade, math_score)
# #     elif grade == 4:
# #         test_score = float(input("Введите баллы за аттестацию: "))
# #         student = FourthGradeStudent(last_name, first_name, grade, test_score)
# #     else:
# #         print("Некорректный класс")
# #
# #     students.append(student)
# #
# # with open(file_name, 'wb') as file:
# #     pickle.dump(students, file)
# #
# # save_students_data("students.bin", 3)





# file = 'database_2.bin'
# database = []
#
#
# class Student:
#     def __init__(self, last_name, first_name, grade):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.grade = grade
#
#
# class FirstGradeStudent(Student):
#     def __init__(self, last_name, first_name, grade, information):
#         super().__init__(last_name, first_name, grade)
#         self.information = information
#
#     def __str__(self):
#         return (f'Имя ученика: {self.last_name}'
#                 f'\nФамилия ученика: {self.first_name}'
#                 f'\nКласс ученика: {self.grade}'
#                 f'\nСкорость чтения: {self.information}')
#
#
# class SecondOrThirdGradeStudent(Student):
#     def __init__(self, last_name, first_name, grade, information):
#         super().__init__(last_name, first_name, grade)
#         self.information = information
#
#     def __str__(self):
#         return (f'Имя ученика: {self.last_name}'
#                 f'\nФамилия ученика: {self.first_name}'
#                 f'\nКласс ученика: {self.grade}'
#                 f'\nДанные итоговой школьной контрольной по математике: {self.information}')
#
#
# class FourthGradeStudent(Student):
#     def __init__(self, last_name, first_name, grade, information):
#         super().__init__(last_name, first_name, grade)
#         self.information = information
#
#     def __str__(self):
#         return (f'Имя ученика: {self.last_name}'
#                 f'\nФамилия ученика: {self.first_name}'
#                 f'\nКласс ученика: {self.grade}'
#                 f'\nБаллы итоговой аттестации: {self.information}')
#
#
# def student_data(n):
#     last_name = input(f'\nВводим данные для ученика номер {n}\nВведите фамилию ученика: ')
#     first_name = input('Введите имя ученика: ')
#     grade = str(input(f'Введите класс в котором обучается {last_name} {first_name} '
#                       f'(в формате <число><буква>, например: "4Г"): '))
#     if grade[:-1] == '1':
#         try:
#             information = int(input(f'Введите скорость чтения для ученика "{last_name} {first_name}" '
#                                     f'(число слов в минуту): '))
#             database.append(FirstGradeStudent(last_name, first_name, grade, information))
#             print(f'Ученик "{last_name} {first_name}" успешно добавлен в базу данных!')
#         except:
#             print(f'Вы ввели некорректные данные для ученика "{last_name} {first_name}". '
#                   f'Его данные не записаны в базу данных!')
#     elif grade[:-1] in ['2', '3']:
#         try:
#             information = float(input(f'Введите данные итоговой школьной контрольной по математике '
#                                       f'(оценка от 1 до 10 баллов) для ученика "{last_name} {first_name}": '))
#             if float(1) <= information <= float(10):
#                 database.append(SecondOrThirdGradeStudent(last_name, first_name, grade, information))
#                 print(f'Ученик "{last_name} {first_name}" успешно добавлен в базу данных!')
#             else:
#                 print(f'Вы ввели некорректные данные для ученика "{last_name} {first_name}". '
#                       f'Его данные не записаны в базу данных!')
#         except:
#             print(f'Вы ввели некорректные данные для ученика "{last_name} {first_name}". '
#                   f'Его данные не записаны в базу данных!')
#     elif grade[:-1] == '4':
#         try:
#             information = float(input(f'Введите данные о баллах за итоговую аттестацию (единый муниципальный тест '
#                                       f'от 1 до 100 баллов) для ученика "{last_name} {first_name}": '))
#             if float(1) <= information <= float(100):
#                 database.append(FirstGradeStudent(last_name, first_name, grade, information))
#                 print(f'Ученик "{last_name} {first_name}" успешно добавлен в базу данных!')
#             else:
#                 print(f'Вы ввели некорректные данные для ученика "{last_name} {first_name}". '
#                       f'Его данные не записаны в базу данных!')
#         except:
#             print(f'Вы ввели некорректные данные для ученика "{last_name} {first_name}". '
#                   f'Его данные не записаны в базу данных!')
#     else:
#         print(f'Вы ввели некорректные данные класса для ученика "{last_name} {first_name}". '
#               f'Его данные не записаны в базу данных!')
#
#
# def write_database():
#     with open(file, 'wb') as f:
#         for i in database:
#             str_write = f'{i.last_name} {i.first_name} {i.grade} {i.information}'
#             f.write(str_write.encode('utf-8') + b'\n')
#
#
# def read_database():
#     with open(file, 'rb') as f:
#         while True:
#             line = f.readline()
#             if not line:
#                 break
#             line_decode = list((line.decode('utf-8').strip()).split())
#             last_name = line_decode[0]
#             first_name = line_decode[1]
#             grade = line_decode[2]
#             if line_decode[2][:-1] == '1':
#                 information = int(line_decode[3])
#                 database.append(FirstGradeStudent(last_name, first_name, grade, information))
#             elif line_decode[2][:-1] == '4':
#                 information = float(line_decode[3])
#                 database.append(FourthGradeStudent(last_name, first_name, grade, information))
#             else:
#                 information = float(line_decode[3])
#                 database.append(SecondOrThirdGradeStudent(last_name, first_name, grade, information))
#
#
# N = int(input('\nВведите N (количество учеников): '))
# for i in range(N):
#     student_data(i+1)
# write_database()
# database = []
# read_database()
# for i in range(len(database)):
#     print(f'\n{i+1}. {str(database[i])}')
#


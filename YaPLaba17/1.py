import random
import sys


class Player:
    def __init__(self):
        self.myNodes = []

    def add_node(self, value):
        self.myNodes.append(value)
        database.append(value)


class Petya(Player):
    def __init__(self):
        super().__init__()


class Vasya(Player):
    def __init__(self):
        super().__init__()


def choosing_a_number_by_computer(high_difficulty=True):
    numbers_list = list(range(1, 2019))
    random.shuffle(numbers_list)

    if not computer.myNodes:
        for i in numbers_list:
            if not (i in database):
                computer.add_node(i)
                return i

    elif len(computer.myNodes) == 1:
        if high_difficulty and len(player.myNodes) >= 2:
            dangerous_number = (player.myNodes[-1] - player.myNodes[-2]) + player.myNodes[-1]
            if (not (dangerous_number in database)) and (1 <= dangerous_number <= 2018):
                computer.add_node(dangerous_number)
                return dangerous_number

        for i in numbers_list:
            the_future_number = ((i - computer.myNodes[-1]) + i)

            if (not (i in database)) and (not (the_future_number in database)) and (1 <= the_future_number <= 2018):
                computer.add_node(i)
                return i

        for i in numbers_list:
            if not (i in database):
                computer.add_node(i)
                return i

    elif len(computer.myNodes) >= 2:
        suitable_number = (computer.myNodes[-1] - computer.myNodes[-2]) + computer.myNodes[-1]
        if (not (suitable_number in database)) and (1 <= suitable_number <= 2018):
            computer.add_node(suitable_number)
            return suitable_number

        if high_difficulty and len(player.myNodes) >= 2:
            dangerous_number = (player.myNodes[-1] - player.myNodes[-2]) + player.myNodes[-1]
            if (not (dangerous_number in database)) and (1 <= dangerous_number <= 2018):
                computer.add_node(dangerous_number)
                return dangerous_number

        for i in numbers_list:
            the_future_number = ((i - computer.myNodes[-1]) + i)

            if (not (i in database)) and (not (the_future_number in database)) and (1 <= the_future_number <= 2018):
                computer.add_node(i)
                return i

        for i in numbers_list:
            if not (i in database):
                computer.add_node(i)
                return i


if __name__ == '__main__':

    database = []

    x = input('\nВыберете игрока (Петя или Вася).\nПетя начнёт первым.\n1. Петя\n2. Вася\nВедите число (1 или 2): ')
    difficulty = input('\nВыберите сложность игры.\n1. Сложная\n2. Лёгкая\nВведите число (1 или 2): ')

    if x == '2':
        player = Vasya()
        computer = Petya()
    else:
        player = Petya()
        computer = Vasya()

    if difficulty == '2':
        difficulty = False
    else:
        difficulty = True

    if isinstance(computer, Petya):
        print(f'\nХод компьютера: {choosing_a_number_by_computer(difficulty)}', end='')

    while True:

        if len(database) >= 2018:
            print('Победа компьютера через окончание доступных вам ходов!')
            sys.exit()

        x = int(input('\nВведите ваше число: '))

        while x in database:
            x = int(input('Данное число уже вводилось\nВведите другое число: '))

        player.add_node(x)

        if (len(player.myNodes) >= 3 and
                (player.myNodes[-1] - player.myNodes[-2]) == (player.myNodes[-2] - player.myNodes[-3])):
            print('\nВы победили!')
            sys.exit()

        if len(database) >= 2018:
            print('Вы победили через окончание доступных компьютеру ходов!')
            sys.exit()

        print(f'Ход компьютера: {choosing_a_number_by_computer(difficulty)}')

        if (len(computer.myNodes) >= 3 and
                (computer.myNodes[-1] - computer.myNodes[-2]) == (computer.myNodes[-2] - computer.myNodes[-3])):
            print('\nПобеда компьютера!')
            sys.exit()

        while len(player.myNodes) >= 4:
            player.myNodes.pop(0)

        while len(computer.myNodes) >= 4:
            computer.myNodes.pop(0)

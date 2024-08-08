import random


def task1(min_limit, max_limit):
    # Сгенерировать случайное целое число от 10 до 99
    return random.randint(min_limit, max_limit)


result = task1(10, 99)
print(result)


def task2(a, b):
    # Сгенерировать случайное действительное число от 1 до 2
    return random.uniform(a, b)


random_number = task2(10, 99)
print(random_number)


def task3(numbers_list):
    # Выбрать случайное число из чисел 1, 5, 8, 9
    return random.choice(numbers_list)


random_list = task3([1, 5, 8, 9])
print(random_list)


def task4(n):
    # Сгенерировать 10 случайных чисел от 1 до 10 и найти их сумму.
    final_amount = 0
    for x in range(1, n + 1):
        x = random.randint(1, 10)
        final_amount += x
    return final_amount


random_amount = task4(10)
print(random_amount)


def task5(min_number, max_number):
    # Сгенерировать случайное четное число от 2 до 20
    return random.randrange(min_number, max_number, 2)


random_even_number = task5(2, 20)
print(random_even_number)


def task6():
    # Показать случайную дату в виде dd.mm.yyyy Например, 01.02.1994
    month = random.randint(1, 12)
    year = random.randint(1990, 2024)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 12:
        day = random.randint(1, 31)
    elif year % 4 != 0:
        day = random.randint(1, 28)
    elif year % 4 == 0:
        day = random.randint(1, 29)
    else:
        day = random.randint(1, 30)
    print(f'{day}.{month}.{year}')


def task7(counter):
    # Показать 10 случайных дат со временем. Например, 01.02.1994 20:24:13
    x = 0
    dates_list = []
    while x <= counter - 1:
        month = random.randint(1, 12)
        year = random.randint(1990, 2024)
        hour = random.randint(1, 23)
        minutes = random.randint(1, 59)
        seconds = random.randint(1, 59)

        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 12:
            day = random.randint(1, 31)
        elif year % 4 != 0:
            day = random.randint(1, 28)
        elif year % 4 == 0:
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 30)
        x += 1
        dates_list.append(f'Год: {day}.{month}.{year} Время: {hour}:{minutes}:{seconds}')
    return dates_list


random_year = task7(10)
print(random_year)


def task8():
    # Сгенерировать 10 квадратных уравнений с целыми коэффициентами, каждое уравнение должно иметь 2 корня.
    # То есть сгенерировать целые числа a, b, c - коэффициенты квадратного уравнения так,
    # чтобы дискриминант был больше 0.
    pass


def task9(n):
    # Сгенерировать список из 10 чисел: 7 нулей и 3 единицы. Единицы расположены на случайных местах в списке.
    new_random_list = []
    counter = 0
    for x in range(n - 1):
        while new_random_list.count(1) < 3:
            new_random_list.append(random.randint(0, 1))
        counter += 1
        new_random_list.append(0)
        if len(new_random_list) == n:
            break
    return new_random_list


new_list = task9(10)
print(new_list)


def task10(subjects):
    # Дан список школьных предметов. Выбрать из него три различных предмета.
    counter = 0
    subjects_list = []
    while counter < 3:
        subjects_list.append(random.choice(subjects))
        counter += 1
    for x in subjects_list:
        if subjects_list.count(x) > 1:
            subjects_list.remove(x)
            subjects_list.append(random.choice(subjects))
    return subjects_list


three_subjects = task10(['физика', 'химия', 'русский', 'математика', 'литература', 'английский'])
print(three_subjects)


def task11(n):
    # Дано число n. Генерировать и показывать случайные целые числа от 1 до 3 до тех пор, пока их сумма меньше n.
    numbers_sum = 0
    random_x_list = []
    while numbers_sum < n:
        random_x = random.randint(1, 3)
        numbers_sum += random_x
        random_x_list.append(random_x)
    return random_x_list


number = task11(10)
print(number)


def task12():
    # Компьютер загадывает число от 1 до 100. У пользователя три попытки отгадать.
    # После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число.
    # Реализовать игру в консоли.
    computer_number = random.randint(1, 100)
    trials = 0
    user_is_winner = True
    while trials < 3:
        user_number = int(input(f'Угадайте целое число от 1 до 100. (Количество попыток - {3 - trials}):'))
        if user_number != computer_number:
            user_is_winner = False
            if user_number < computer_number:
                print(f'Число {user_number} меньше загаданного')
            else:
                print(f'Число {user_number} больше загаданного')
        else:
            user_is_winner = True
            break
        trials += 1
    if user_is_winner:
        print('Пользователь выиграл')
    else:
        print('Выиграл компьютер')


def task13(n):
    # Игра. Дано число n. Например, n = 10.
    # Пользователь и компьютер по очереди называют целое число от 1 до 3 до тех пор,
    # пока сумма названых чисел меньше n. Как только сумма становится равной n,
    # то игра заканчивается и выигрывает тот, кто сделал последний ход,
    # то есть назвал последнее число. Реализовать игру в консоли.
    sum_of_numbers = 0
    last_move = None
    while sum_of_numbers < n:
        user_number = int(input("Введите число от 1 до 3: "))
        sum_of_numbers += user_number
        last_move = 'пользователь'
        computer_number = random.randint(1, 3)
        sum_of_numbers += computer_number
        last_move = 'компьютер'
    if last_move == 'пользователь':
        return "Пользователь выиграл!"
    else:
        return "Компьютер выиграл!"


game_number = task13(10)
print(game_number)

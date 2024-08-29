import math


def task1():
    # Дан список чисел. Найти наименьшее число в нем.
    a = [2, 4, -3, 3, 8, 1]
    minimum_number = a[0]
    for x in a:
        if x < minimum_number:
            minimum_number = x
    print('Наименьшее число: ', minimum_number)


def task2():
    # Дан список чисел. Найти сумму четных чисел в нем.
    a = [1, 2, 3, 4, 5, 6]
    sum = 0
    for x in a:
        if x % 2 == 0:
            sum += x
    print(sum)


def task3():
    # Дан список чисел. Вывести yes, если сумма четных
    # больше суммы нечетных, иначе no
    a = [1, 2, 3, 4, 5, 6]
    sum_2 = 0
    sum_3 = 0
    for x in a:
        if x % 2 == 0:
            sum_2 += x
        else:
            sum_3 += x
    if sum_2 > sum_3:
        print('Yes')
    else:
        print('No')


def task4():
    # Дан список чисел. Вывести на экран те числа,
    # которые больше первого числа списка
    a = [2, 4, 0, 3, 8, 1]
    for x in a:
        if x > a[0]:
            print(x)


def task5():
    # Дан список чисел. Вывести на экран четные числа,
    # которые меньше суммы первого и последнего чисел списка.    
    a = [2, 4, 0, 3, 8, 1]
    sum = a[0] + a[-1]
    for x in a:
        if x < sum and x % 2 == 0 and x != 0:
            print(x)


def task6():
    # Дан список. Определить, сколько раз в нем содержится данное
    # число.
    a = [2, 4, 0, 3, 8, 1]
    n = int(input('Введите целое число: '))
    sum = 0
    for x in a:
        if x == n:
            sum += 1
    print(f'Количество повторений заданного числа ({n}) = {sum}')


def task7():
    # Дан список. Вывести yes, если все числа равны, иначе no
    a = [2, 2, 2, 2, 2, 2]
    # 1 способ: max = 8, min = 1
    # [2, 2, 2, 2, 2] max = 2 min = 2
    # 2 способ
    is_equal = True
    for x in a:
        if x != a[0]:
            is_equal = False
            break

    if is_equal:
        print('yes')
    else:
        print('no')


# Нерешенное задание с предыдущего дз
def task10():
    # Найдите хотя бы одно натуральное число,
    # которое делится на 11, а при делении на 2, 3, 4, ...,
    # 10 дает в остатке 1.
    n = 1
    while True:
        is_success = True

        if n % 11 != 0:
            is_success = False
        else:
            for k in range(2, 11):
                if n % k != 1:
                    is_success = False
                    break

        if is_success:
            print(n)
            break

        n += 1


def task11():
    # Найдите 3 натуральных числа, больших 100000,
    # которое делится на 11, а при делении на 2, 3, 4, ...,
    # 10 дает в остатке 1.
    n = 100001
    FIND_COUNT = 3
    counter = 0
    while True:
        is_success = True

        if n % 11 != 0:
            is_success = False
        else:
            for k in range(2, 11):
                if n % k != 1:
                    is_success = False
                    break

        if is_success:
            print(n)
            counter += 1
            if counter == FIND_COUNT:
                break

        n += 1


def gen_exam_table():
    TASK_COUNT = 25
    min_year = 2002
    max_year = 2023

    print(" ", end=" ")
    for task_number in range(TASK_COUNT):
        print(task_number + 1, end=" ")
    print()

    for year in range(min_year, max_year + 1):
        zero_row = "0 " * TASK_COUNT
        for postfix in ["-1", "-2", "-3", "-F"]:
            print(str(year) + postfix, zero_row)


gen_exam_table()

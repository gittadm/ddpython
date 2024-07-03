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
        else:
            continue
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
        elif x == 0:
            continue


def task6():
    # Дан список. Определить, сколько раз в нем содержится данное
    # число.
    a = [2, 4, 0, 3, 8, 1]
    n = int(input('Введите целое число: '))
    sum = 0
    for x in a:
        if x == n:
            sum += 1
    print(f'Колличество повторений заданного числа ({n}) = {sum}')


def task7():
    # Дан список. Вывести yes, если все числа равны, иначе no
    a = [2, 4, 0, 3, 8, 1]
    for x in a:
        if x == a[0]:
            print('yes')
        else:
            print('no')


# Нерешенное задание с предыдущего дз
def task10():
    # Найдите хотя одно натуральное число,
    # которое делится на 11, а при делении на 2, 3, 4, ...,
    # 10 дает в остатке 1.
    n = math.inf
    for i in range(1, n):
        for y in range(2, 11):
            if i % 11 == 0 and (i % y == 1):
                print(i)
                n += 1
            else:
                n += 1
    # не поняла как решить задачу
    pass

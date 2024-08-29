def task1():
    # Дан список чисел. Показать все отрицательные числа с четными индексами.
    a = [1, 2, -3, -4, 5, 6, -7, 8, -9, -10]
    b = [x for x in a if x % 2 == 0]
    c = []

    for x in b:
        if x < 0:
            c.append(x)
    print(c)


def task2():
    # Дан список чисел. Выведите все элементы списка, каждый из которых больше своего предыдущего элемента.
    a = [1, 2, 1, 4, 5, 6, 6, 9, 8, 10]
    b = []

    for index, x in enumerate(a):
        if x != a[0] and a[index] > a[index - 1]:
            b.append(x)
    print(b)


def task3():
    # Дан список чисел. Выведите все наибольшие числа и их индексы.
    a = [10, 2, 10, 4, 10, 6, 7, 8, 9, 10]
    b = a.copy()
    a.sort()
    max_number = a[-1]

    for index, x in enumerate(b):
        if x == max_number:
            print(f'Наибольшее число = {x}, индекс числа = {index}')


def task4():
    # Дан список чисел. Определите, сколько в этом списке элементов, каждый из которых больше двух своих соседей.
    a = [1, 3, 2, 3, 4, 1, 7, 8]
    b = []

    for index, x in enumerate(a):
        if x != a[0] and a[index] > a[index - 1] and a[index] > a[index - 2]:
            b.append(x)
    print(b)


def task5():
    # Дан список чисел. Преобразовать список так, чтобы сначала шли нули, далее четные числа, далее нечетные.
    a = [1, 2, 3, 4, 5, 6, 0, 7, 8, 0, 9, 10]
    even_numbers = [x for x in a if x % 2 == 0 and x != 0]
    zeros = [x for x in a if x == 0]
    uneven_numbers = [x for x in a if x % 2 != 0]
    print(zeros + even_numbers + uneven_numbers)


def task6():
    # Дан список чисел и число k>0. Выведите те пары чисел из списка, которые отличаются на k.
    a = [6, 2, 5, 4, 8, 0, -3, 8]
    k = 3
    for index, x in enumerate(a):
        if index + k == len(a):
            break
        else:
            print(x, a[index + k])


def task7():
    # Даны 2 списка чисел. Найти числа, которые принадлежат обоим спискам
    # и которые меньше суммы всех чисел первого списка.
    a = [1, 3, 2]
    b = [1, 2, 3, 4, 5, 6, 7, 8]

    for x in a:
        for y in b:
            if y == x and y < sum(a):
                print(y)


def task8():
    # Даны 3 списка чисел. Найти числа из 3 списка, которые можно представить
    # в виде суммы двух чисел, первое - из 1 списка, второе - из 2 списка.
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    c = [12, -3, 0, 7]
    found_numbers = []

    for x in a:
        for y in b:
            summ = x + y
            if summ in c and summ not in found_numbers:
                found_numbers.append(summ)
    print(found_numbers)


def task9():
    # Даны 2 списка одинаковой длины. Получить новый список как их разность -
    # числа на соответствующих местах вычитаются (от первого списка второй).
    a = [1, 0, 6, 8]
    b = [-5, 3, -10, 8]
    index = [x for x in range(len(a))]
    c = []

    for x in index:
        c.append(a[x] - b[x])
    print(c)


def task10():
    # Вася хочет узнать, какую оценку он получит в четверти по информатике.
    # Учитель придерживается следующей системы: вычисляется среднее арифметическое всех оценок в журнале,
    # и ставится ближайшая целая оценка, не превосходящая среднего арифметического.
    # При этом если у школьника есть двойка, а следующая за ней оценка – не двойка, то двойка считается закрытой,
    # и при вычислении среднего арифметического не учитывается. Дан список оценок - целые числа от 2 до 5 включительно.
    # Найдите четвертную оценку.
    grades = [2, 5, 3, 4]
    updated_grades = []

    for index, x in enumerate(grades):
        if index + 1 < len(grades) and grades[index] < grades[index + 1] and grades[index] == 2:
            updated_grades.append(0)
        else:
            updated_grades.append(x)

    if 0 in updated_grades:
        denominator = len(updated_grades) - 1
    else:
        denominator = len(updated_grades)
    final_grade = sum(updated_grades)
    final_grade /= denominator
    print(round(final_grade))


def task11():
    # Дан список чисел. Определить, является ли он симметричным, то есть читается
    # одинаково справа налево и слева направо. Например, [1, 3, 4, 3, 1] - симметричный.
    a = [6, 2, 3, 1, 2, 6]
    is_symmetric = bool

    for index, x in enumerate(a):
        if a[index] != a[len(a) - 1 - index]:
            is_symmetric = False
            break
        else:
            is_symmetric = True
    if is_symmetric:
        print('Список симметричный')
    else:
        print('список не является симметричным')


def task12():
    # Дан список. Найти сумму первого и последнего чисел. Найти сумму первых двух и последних двух чисел списка.
    a = [1, 2, 3, 4, 5, 6]
    print(a[0] + a[-1], a[0] + a[1], a[-1] + a[-2])


def task13():
    # Дан список. Вывести все пары соседних чисел. Например, для [5, 7, 3, 2] это 5, 7 и 7, 3 и 3, 2
    a = [5, 7, 3, 2]
    for index, x in enumerate(a):
        if a[index] == a[-1]:
            break
        else:
            print(a[index], a[index + 1])


def task14():
    # Дан список. Заменить все нулевые числа на 1
    a = [1, 0, 3, 0, 5, 6, 0, 0]
    for index, x in enumerate(a):
        if a[index] == 0:
            a[index] = 1
    print(a)


def task15():
    # Дан список. Найти кол-во отрицательных чисел
    a = [1, -2, -3, 4, -5, 6, -7, 8, 9, -10]
    counter = 0

    for x in a:
        if x < 0:
            counter += 1
    print(counter)


def task16():
    # Дан список. Если в нем отрицательных чисел больше чем положительных, то вывести Yes иначе No
    a = [1, -2, -3, 4, -5, 6, -7, 8, 9, -10]
    positive_counter = 0
    negative_counter = 0

    for x in a:
        if x < 0:
            negative_counter += 1
        else:
            positive_counter += 1
    if negative_counter > positive_counter:
        print('yes')
    else:
        print('no')


def task17():
    # Дан список. Вывести на экран числа, которые находятся на четных позициях
    a = [1, -2, -3, 4, -5, 6, -7, 8, 9, -10]

    for index, x in enumerate(a):
        if index % 2 == 0 and index != 0:
            print(x)


def task18():
    # Дан список. Обменять значения крайних элементов. То есть [5, 7, 3, 1] -> [1, 7, 3, 5]
    a = [5, 7, 3, 1]
    b = a.copy()
    a[0] = b[-1]
    a[-1] = b[0]
    print(a)

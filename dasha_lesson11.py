def task1(a):
    # Task 1
    # Дан кортеж чисел. Выведите кол-во чисел в кортеже, первый элемент, последний элемент, наибольший элемент,
    # наименьший элемент, сумму всех чисел.
    results = {
        'Кол-во чисел': len(a),
        '1-й элемент': a[0],
        'Последний элемент': a[-1],
        'Наибольший элемент': max(a),
        'Наименьший элемент': min(a),
        'Сумма чисел': sum(a),
    }
    return results


c = task1((10, -2, 3, 14, 0, 4))
print(c)


def task2(a, k):
    # Дан кортеж чисел a. Определите, содержит ли кортеж данное число k.
    if k in a:
        return 'Yes'

    return 'No'


result = task2((2, 4, 5, 8), 8)
print(result)


def task3(b):
    # Дан кортеж чисел. Найти сумму четных элементов
    numbers_sum = 0
    for x in b:
        if x % 2 == 0:
            numbers_sum += x
    return numbers_sum


result = task3((1, 2, 3, 4, 5))
print(result)


def task4(a):
    # Дан кортеж чисел. Найти сумму элементов, которые больше 4 и у которых индекс четный.
    new_tuple = [x for index, x in enumerate(a) if index % 2 == 0 and x > 4]
    return sum(new_tuple)


result_sum = task4((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(result_sum)


def task5(a):
    # Дан кортеж чисел. Найдите, сколько раз каждое число встречается в кортеже.
    # Например, для (6, 4, 6, 3, 4) ответ: 6 - 2, 3 - 1, 4 - 2
    numbers_counter = {}
    for x in a:
        numbers_counter.update({x: a.count(x)})
    return numbers_counter


y = task5((6, 4, 6, 3, 4))
print(y)


def task6(a, b):
    # Даны два кортежа чисел. Определить, состоят ли они из одних и тех же чисел
    # (порядок чисел в кортеже и кол-во повторов чисел не важны). Например, (1, 4, 1, 6) и (1, 6, 6, 1) - да
    is_exist = False
    for x in a:
        if x in b:
            is_exist = True
    if is_exist:
        answer = 'Yes'
    else:
        answer = 'No'
    return answer


result = task6((1, 4, 1, 6), (1, 6, 6, 1))
print(result)


def task7(number):
    # Создать пустое множество. Добавить в него числа от 1 до 10. Вывести на экран.
    # Проверить, содержит ли данное множество данное число.
    is_exist = bool
    answer = str
    a = {x for x in range(1, 11)}
    for x in a:
        if number == x:
            is_exist = True
            break
        elif number not in a:
            is_exist = False
    if is_exist:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


k = task7(15)
print(k)


def task8(a):
    # Дано множество чисел. Удалить из него все четные числа.
    b = set()
    for x in a:
        if x % 2 != 0:
            b.add(x)
    return b


a = task8({1, 2, 3, 4, 5, 6, 7, 8})
print(a)


def task9(a):
    # Дано множество чисел. Увеличить в нем все нечетные числа в 2 раза.
    b = set()
    for x in a:
        if x % 2 != 0:
            b.add(x * 2)
        else:
            b.add(x)
    return b


b = task9({1, 2, 3, 4, 5, 6, 7, 8})
print(b)


def task10(a, b):
    # Даны два множества чисел. Получить множество, состоящее из общих чисел обоих множеств,
    # то есть найти пересечение множеств.
    c = set()
    c = a.intersection(b)
    return c


result = task10({1, 2, 3}, {4, 3, 2})
print(result)


def task11(a, b, c):
    # Даны три множества. Вывести на экран те числа, которые содержатся во всех трех множествах.
    d = set()
    e = set()
    d = a.intersection(b)
    e = c.intersection(d)
    return e


result = task11({1, 2, 3}, {4, 3, 2}, {2, 6, 10})
print(result)


def task12(a, b, c):
    # Даны три множества. Вывести на экран те числа, каждое из которых содержится только в каком-то одном из множеств.
    d = a.difference(b, c)
    e = b.difference(a, c)
    f = c.difference(a, b)
    g = d.union(e, f)
    return g


result = task12({1, 2, 3}, {4, 3, 2}, {2, 6, 10})
print(result)


def task13(surnames):
    # Дан список фамилий. Найти кол-во однофамильцев. Например,
    # ['ivanov', 'petrov', 'ivanov', 'petrov', 'ivanov', 'petrov'] - 6,  ['ivanov', 'petrov', 'ivanov'] - 2,
    # ['ivanov', 'petrov'] - 0
    surname_count = {}
    for surname in surnames:
        if surname in surname_count:
            surname_count[surname] += 1
        else:
            surname_count[surname] = 1
    for surname, count in surname_count.items():
        return count


result = task13(['ivanov', 'petrov', 'ivanov', 'petrov', 'ivanov', 'petrov'])
print(result)


def task14():
    # Дан список, элементами которого являются множества, содержащие фамилии учеников. Например,
    # a = [{'ivanov', 'petrov'}, {'ivanov', 'sidorov'}, {'ivanov', 'petrov', 'leonov'}]
    # Найти учеников, которые есть в каждом множестве. Найти учеников, которые есть только в одном множестве.
    # Найти учеников, которые есть только в 2 множествах. Найти учеников, которые есть только в k (k - число дано)
    # множествах.
    pass

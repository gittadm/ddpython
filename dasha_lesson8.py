# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

def task1():
    # Дан список. Удалить последний и первый элементы.
    a = [1, 2, 3, 4, 5, 6]
    a.pop(0)
    a.pop()
    print(a)


def task2():
    # Дан список. Удалить все нули.
    a = [0, 2, 0, 4, 0, 6]
    for x in a:
        a.remove(x)
    print(a)


def task3():
    # Дан список. Вставить после каждого четного числа ноль.
    a = [1, 2, 3, 4, 5, 6]
    new_list = []

    for x in a:
        new_list.append(x)
        if x % 2 == 0:
            new_list.append(0)

    print(new_list)


def task4():
    # Даны два списка одинаковой длины. Получить новый список как их сумму -
    # числа на соответствующих местах суммируются.
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    counter = [i for i in range(len(a))]
    c = []

    for i in counter:
        x = a[i]
        y = b[i]
        c.append(x + y)
    print(c)


def task5():
    # Даны два списка. Показать те числа, которые есть в обоих списках.
    a = [1, 2, 3, 4]
    b = [5, 4, 7, 2]
    c = []
    for x in a:
        for y in b:
            if x == y:
                c.append(x)
    print(c)


def task6():
    # Даны три списка. Показать те числа, которые есть в первых двух списках, но нет в третьем.
    a = [1, 2, 3, 4]
    b = [5, 4, 7, 2]
    c = [9, 10, 4, 12]
    d = []
    for x in a:
        for y in b:
            if x == y:
                d.append(x)
    d = [x for x in d if x not in c]
    print(d)


def task7():
    # Дан список. Определить, если ли в нем повторяющиеся числа.
    a = [1, 2, 3, 4, 5, 6]
    result = False
    for x in a:
        if a.count(x) > 1:
            result = True
            break
    if result:
        print('Yes')
    else:
        print('No')


def task8():
    # Дан список. Найти в нем два наименьших числа.
    a = [6, 8, 12, -1, 5, 7]
    a.sort()
    print(a[0], a[1])

# Дан список. Удалить последний и первый элементы.

def del_elements(a):
    a.remove(a[0])
    a.pop()
    print(a)
    return 2


del_elements(['bbq', 'explosion', 'radiation', 'X-RAY sickness', 'happy'])
del_elements(['X-RAY sickness', 'happy'])
x = del_elements(['bbq'])

# Дан список. Удалить все нули.
def del_emptiness():
    unit = [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 5, 7, 8, 9, 6, 3, 0, 2, 4, 2]
    zero_unit = []
    for number in unit:
        if number > 0:
            zero_unit.append(number)
    print(zero_unit)


# Дан список. Вставить после каждого четного числа ноль.
def insert_0(unit):
    numbers = []
    for number in unit:
        if number % 2 == 0:
            numbers.append(number)
            numbers.append(0)
        else:
            numbers.append(number)
    return numbers


numbers2 = insert_0([3, 6, 98, 7, 1, 5, 4, 7, 98, 5, 4, 2, 3, 5, 4, 55, 85, 8, 4, 54, 8, 4, 5, 54, 6, 8, 6, 9, 6])
print(numbers2)

# Даны два списка. Показать те числа, которые есть в обоих списках.


def both_in_queue():
    first_queue = [4, 5, 54, 5, 2, 4, 7]
    second_queue = [4, 5, 54, 5, 6, 21]
    output_queue = []
    for number in first_queue:
        for number_1 in second_queue:
            if number == number_1:
                output_queue.append(number)
    print(output_queue)


# Даны два списка одинаковой длины. Получить новый список как их сумму - числа на соответствующих местах суммируются.

# РЕШИЛ НЕ САМ, ТОЛЬКО С ПОМОЩЬЮ ДАШИ, НЕ ПОНЯЛ ПОЧТИ НИЧЕГО
def q_summ():
    mylist = [5, 8, 5, 87, 9, 6]
    mylist_1 = [5, 8, 5, 87, 9, 6]
    mylist_summ = []
    counter = []
    for index, number in enumerate(mylist):
        counter.append(index)
    for index in counter:
        a = mylist[index]
        b = mylist_1[index]
        mylist_summ.append(a + b)
    print(mylist_summ)


# Даны три списка. Показать те числа, которые есть в первых двух списках, но нет в третьем.
def task_three_lists():
    mylist = [1, 3, 9, 4, 1, 1]
    mylist_1 = [4, 8, 1, 3, 1]
    mylist_2 = [8, 1, 4, 0, 2]
    hidden_list = []
    for number in mylist:
        for number_1 in mylist_1:
            if number == number_1 and number not in hidden_list:
                hidden_list.append(number)

    for number_2 in mylist_2:
        for number_3 in hidden_list:
            if number_2 == number_3:
                hidden_list.remove(number_2)

    print(hidden_list)

    a = [1, 1, 3, 4, 1, 1, 1, 3, 3, 3, 1, 5, 4, 5]
    unique_numbers = []

    for number in a:
        if number not in unique_numbers:
            unique_numbers.append(number)


# Дан список. Найти в нем два наименьших числа.
def minimal_number():
    mylist = [13, 5, 8, 9, 1, 4, 0.2, 6, 8, 44, 1, 0]
    mylist.sort()
    print(mylist[0], mylist[1])

    mylist = [5, 4, 3, 1, 2, 1, 4, 3, 1, 5, 5, 5]
    #                  3
    b = []

    # print(mylist[len(mylist) - 1])

    # поиск наименьшего числа и его индекса
    min = mylist[0]
    i_min = 0
    for index, x in enumerate(mylist):
        if x < min:
            min = x
            i_min = index

    # a[i_min]

    min = mylist[0]
    b.append(min)
    for x in mylist:
        if x < min:
            min = x
            b.append(min)

    # b: 5, 4, 3, 2, 1

    print(b[len(b) - 1], b[len(b) - 2])
    # print(b[-1], b[-2])

    # b = [7, 5, 4, 9, 8]
    # print(b[2])
    # last_index = len(b) - 1
    # print(b[last_index])

    # min: 5, 4, 3, 2, 1
    # 5 4 3 2 1

    print(min)


# Дан список. Определить, если ли в нем повторяющиеся числа.
def doubled_numbers():  # НЕ УСПЕЛ РЕШИТЬ, ДОЛГО ДУМАЛ. ХОТЕЛ СНАЧАЛА ПО ИНДЕКСАМ СРАВНИТЬ ЧИСЛА, МОЛ,
    # ЕСЛИ ЗНАЧЕНИЕ У ИНДЕКСОВ ОДИНАКОВОЕ, ТО ВЫВЕСТИ "ДА", НО ТАК И НЕ ПОНЯЛ КАК РЕАЛИЗОВАТЬ
    mylist = [0, 2, 3, 4, 0, 4]
    for number in mylist:
        return len(mylist) != len(set(mylist))


doubled_numbers()

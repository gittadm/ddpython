# Дан список. Удалить последний и первый элементы.

def del_elements():
    object_class_a = ['bbq', 'explosion', 'radiation', 'X-RAY sickness', 'happy']
    object_class_a.remove(object_class_a[0])
    object_class_a.pop()
    print(object_class_a)


# Дан список. Удалить все нули.
def del_emptiness():
    unit = [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 5, 7, 8, 9, 6, 3, 0, 2, 4, 2]
    zero_unit = []
    for number in unit:
        if number > 0:
            zero_unit.append(number)
    print(zero_unit)


# Дан список. Вставить после каждого четного числа ноль.
def insert_0():
    unit = [3, 6, 98, 7, 1, 5, 4, 7, 98, 5, 4, 2, 3, 5, 4, 55, 85, 8, 4, 54, 8, 4, 5, 54, 6, 8, 6, 9, 6]
    numbers_list = []
    for number in unit:
        if number % 2 == 0:
            numbers_list.append(number)
            numbers_list.append(0)
        else:
            numbers_list.append(number)
    print(numbers_list)


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
    queue = [5, 8, 5, 87, 9, 6]
    queue_1 = [5, 8, 5, 87, 9, 6]
    queue_summ = []
    counter = []
    for number in range(len(queue)):
        counter.append(number)
    for number in counter:
        a = queue[number]
        b = queue_1[number]
        queue_summ.append(a + b)

    print(queue_summ)

# Даны три списка. Показать те числа, которые есть в первых двух списках, но нет в третьем.



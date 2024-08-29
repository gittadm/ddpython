# Дан список чисел. Показать все отрицательные числа с четными индексами.
def task2():
    mylist = [0, 0, 8, -8, 60, 59, -17, -56, 14]
    index_list = []
    hidden_list_2 = []
    for index, number in enumerate(mylist):
        if index % 2 == 0 and number < 0:
            index_list.append(index)
            hidden_list_2.append(number)
    print(hidden_list_2)


# Дан список чисел. Выведите все элементы списка,
# каждый из которых больше своего предыдущего элемента.
def task3(mylist): # НЕ ПОНИМАЮ ПОЧЕМУ ПРЕРЫВАЕТСЯ ФУНКЦИЯ ПОСЛЕ ДОБАВЛЕНИЯ ЧИСЛА КОТОРОЕ ОЧЕВИДНО БОЛЬШЕ ПРЕДЫДУЩЕГО
    new_list = []
    for index, number in enumerate(mylist):
        if index > 0 and mylist[index] > mylist[index - 1]:
            new_list.append(number)
    return new_list

# p = task3([1000000, 0, 1, 2, -3, 4, 8, 4, 0, 0, 0, 9, -3, 0, 1])
# print(p)

# Дан список. Вывести все пары соседних чисел. Например, для [5, 7, 3, 2] это 5, 7 и 7, 3 и 3, 2

def task14():
    mylist = [5, 4, 8, 12, 16, 23, 42]
    counter = 0
    pairs_of_numbers = []
    exist = False
    for index in range(len(mylist) - 1):
        if mylist[index + 1] != exist:
            pairs_of_numbers.append(mylist[index + 1])
            counter += 1
            if counter == 2:
                print(pairs_of_numbers)
                counter -= 1
                pairs_of_numbers.pop(0)


# Дан список. Заменить все нулевые числа на 1

def task15():
    mylist = [-1, -5, 0, 4, 0, -8, 0, 12, 0, 16, 0, 23, 0, 42]
    new_list = []
    for number in mylist:
        if number == 0:
            number += 1
            new_list.append(number)
        else:
            new_list.append(number)
    print(new_list)


# Дан список. Найти кол-во отрицательных чисел
def task16():
    mylist = [-1, -5, 0, 4, 0, -8, 0, 12, 0, 16, 0, -23, 0, 42]
    zero_list = []
    for number in mylist:
        if number < 0:
            zero_list.append(number)
    print(len(zero_list))


# Дан список. Если в нем отрицательных чисел больше чем положительных, то вывести Yes иначе No
def task17():
    mylist = [-1, -5, 0, 4, 0, -8, 0, 12, 0, 16, 0, -23, 0, 42]
    positive_number = []
    negative_number = []
    for number in mylist:
        if number < 0:
            negative_number.append(number)
        elif number > 0:
            positive_number.append(number)
    if len(negative_number) > len(positive_number):
        print('Yes')
    else:
        print('No')


# Дан список. Вывести на экран числа, которые находятся на четных позициях
def task18():
    mylist = [4, 8, 12, 16, 23, 42]
    for index, number in enumerate(mylist):
        if index % 2 == 0:
            print(number, end=' ')


# Дан список. Обменять значения крайних элементов. То есть [5, 7, 3, 1] -> [1, 7, 3, 5]
def task19():
    mylist = [5, 7, 3, 1]
    x = mylist[0]
    y = mylist[len(mylist) - 1]

    mylist[0] = y
    mylist[len(mylist) - 1] = x

    print(mylist)

    # first_two = []
    # for index, number in enumerate(mylist):
    #     if index == 0:
    #         first_two.append(number)
    #         mylist.pop(index)
    #     if index == 1:
    #         first_two.append(number)
    #         mylist.pop(index)
    # mylist.reverse()
    # first_two.reverse()
    # print(mylist + first_two)

task19()

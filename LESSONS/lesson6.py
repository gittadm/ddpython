def task5():
    user_write = int(input('Write any N number: '))
    for i in range(1, user_write):
        if i % 3 == 0:
            print(i)

    for i in range(1, 9):
        if i % 3 == 0:
            print(i)

    if 2 % 3 == 0:
        print(2)
    if 3 % 3 == 0:
        print(3)
    if 4 % 3 == 0:
        print(4)
    if 5 % 3 == 0:
        print(5)
    if 6 % 3 == 0:
        print(6)
    if 7 % 3 == 0:
        print(7)
    if 8 % 3 == 0:
        print(8)

def task1():
    a = [2, [1, 2, 3], 'e', True, 0, 0, 1, 1, 10, 10]
    b = [[1, 2, 0], [4, 4, 5]]

    print(a[1:4])
    print(a[1][2])

    c = [1, 2, 3, 4, 5, 6]
    #    0  1  2  3  4  5

    print(c[c[2]])
    print(len(c))  # длина списка (кол-во элементов)

    c[0] = c[2] + c[3] - c[4]

    print(c)

    print(c[len(c) - 1])  # последний элемент в списке
    print(c[-1])

    # print(a[40]) # error

def task2():
    a = [1, 4, 2, 5, 6, 3]
    # найти сумму всех чисел
    sum = 0
    for x in a:
        sum += x
        print(x)
    print('Sum', sum)

    # найти наибольшее число в списке
    max = a[0]

    for x in a:
        if x > max:
            max = x

    print('Max', max)
task2()
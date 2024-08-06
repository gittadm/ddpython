# Дан кортеж чисел. Выведите кол-во чисел в кортеже, первый элемент, последний элемент,
# наибольший элемент, наименьший элемент, сумму всех чисел.


# ИЛИ МОЖНО ДОБАВИТЬ ДОПОЛНИТЕЛЬНУЮ ФУНКЦИЮ НА НАХОЖДЕНИЕ МИНИМАЛЬНОГО ЧИСЛА ВМЕСТО MIN

# def task3_2(numbers):
#     min_number = numbers[0]
#     for number in numbers:
#         if number < min_number:
#             min_number = number
#     return min_number

def task3_1(numbers):
    total_summ = 0
    for number in numbers:
        total_summ += number
    return total_summ


def task3(numbers):
    biggest_number = numbers[0]
    for number in numbers:
        if number > biggest_number:
            biggest_number = number

    return biggest_number


numbers = (555, 963, 489, 48, 59, -4)
length = len(numbers)
first_number = numbers[0]
last_number = numbers[-1]
minimal = min(numbers)
# result_for_min_number = task3_2(numbers)
result = task3_1(numbers)
print(f'\n Length = {length} \n First Number = {first_number} \n Last Number = {last_number} '
      f'\n Biggest Number = {task3(numbers)} \n Minimal Number = {minimal} \n Result = {result}')
      #f'\n Minimal Number = {result_for_minimal_number}')



# Дан кортеж чисел a. Определите, содержит ли кортеж данное число k.
def task4(a, k):
    for num in a:
        if num == k:
            return f'Number {num} was found'
    return f'Number {k} not found'

a = (0, 15, 48, 92, -2, -4, 2)
k = -65

result = task4(a, k)
print(result)


# Дан кортеж чисел. Найти сумму четных элементов
def task_5(even_numbers):
    total = 0
    for number in even_numbers:
        if number % 2 == 0:
            total += number
    return total

even_numbers = (51, 47, -48, 3, 48, 32, -68, 96)
result = task_5(even_numbers)
print(f' Total summ = {result}')


# Дан кортеж чисел. Найти сумму элементов, которые больше 4 и у которых индекс четный

def task_6(elements):
    MAX = 4
    total = 0
    for index, unit in enumerate(elements):
        if unit > MAX and index % 2 == 0:
            total += unit
    return total

elements = (51, 47, -48, 3, 48, 32, -68, 96)
result = task_6(elements)
print(result)

def task7(elements):
    # Дан кортеж чисел. Найдите, сколько раз каждое
    # число встречается в кортеже.
    # Например, для (6, 4, 6, 3, 4)
    # ответ: 6 - 2, 3 - 1, 4 - 2
    meeting = {}
    for unit in elements:
        if unit in meeting:
            meeting[unit] += 1
        else:
            meeting[unit] = 1

    return meeting

elements = (0, 15, 15, 0, 15, 14, 0, 0)
result = task7(elements)
print(result)
print('$' * 20)

# Даны два кортежа чисел. Определить, состоят ли они из
# одних и тех же чисел
# (порядок чисел в кортеже и кол-во повторов чисел не важны).
# Например, (1, 1, 6) и (1, 6, 6, 1, 8) - да
# s1 = {1, 6} // 2 способ
# s2 = {1, 6, 8}
def task8(data, data1):
    for number in data:
        if number not in data1:
            return 'No'
    for number in data1:
        if number not in data:
            return 'No'
    return 'Yes'

data = (1, 1, 6)
data1 = (1, 6, 6, 1)

result = task8(data, data1)
print(result)
print('-' * 30)


def task9(unit):
    numbers = set()
    for number in range(1, 10):
        numbers.add(number)
    if unit in numbers:
        print('Yes')
    if unit not in numbers:
        print('No')
    return numbers
unit = 4
result = task9(unit)
print(result)


# Дано множество чисел. Удалить из него все четные числа.
def task10(data):
    set_of_numbers = set()
    for number in data:
        set_of_numbers.add(number)
    odd_numbers = set()
    for number in set_of_numbers:
        if number % 2 != 0:
            odd_numbers.add(number)
    return odd_numbers


data = list(range(1, 23))
result = task10(data)
print(result)

# Дано множество чисел. Увеличить в нем все нечетные числа в 2 раза.
def task11(serial_of_numbers, multiplier = 2):
    set_of_numbers = set()
    multiplier_set_of_numbers = set()
    for number in serial_of_numbers:
        set_of_numbers.add(number)
        if number % 2 != 0:
            number *= multiplier
            multiplier_set_of_numbers.add(number)

    return multiplier_set_of_numbers


multiplier = 2
serial_of_numbers = list(range(1, 8))
result = task11(serial_of_numbers, multiplier)
print(result)

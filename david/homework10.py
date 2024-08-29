# Создать словарь, который хранит информацию о книге: название - Мартин Иден,
# автор - Джек Лондон, год издания - 2012, кол-во страниц - 170, издательство - Бином.

def task3():
    dict.book_info = {
        'name': 'Martin Iden',
        'author': 'Jack London',
        'publishing': '2012',
        'publisher': 'Binom'
    }


# Создать пустой словарь. Вывести словарь на экран. Добавить значение 2000 с ключом year.
# Вывести словарь на экран. Добавить значение 'BMW' с ключом model. Вывести словарь на экран.
# Удалить значение с ключом year. Вывести словарь на экран. Изменить BMW на Audi. Вывести словарь на экран.

def task4():
    car_info = {}
    car_info.update({
        'year': '2000',
        'model': 'BMW',
    })
    car_info.pop('year')
    car_info['model'] = 'Audi'
    return car_info


# result = task4()
# print(result)


#  Дан словарь man = {'name': 'Ivan', 'age': 20}. Вывести на экран список ключей, то есть name, age.
#  Вывести на экран список значений, то есть Ivan, 20. Создать копию словаря в переменную person.
#  Очистить исходный словарь man.
def task5():
    man = {
        'name': 'Ivan',
        'age': '20'
    }
    keys_info = man.keys()
    values_list = man.values()
    person = man.copy()
    man.clear()
    return keys_info, values_list, person


# result = task5()
# print(result)

# Дан словарь man = {'name': 'Ivan', 'languages': ['php', 'java', 'python']}.
# Вывести на экран кол-во языков программирования, которыми владеет Ivan.
def task6(man):
    number_of_languages = man['languages']
    return len(number_of_languages)

task6({
        'name': 'Ivan',
        'languages': ['php', 'java', 'python']
    })
task6({
        'name': 'Petr',
        'languages': ['php', 'java', 'python']
    })

def len2():
    a = [1, 2]
    return 2


a = [1, 4, 5]
b = [3, 5]

print(len(a))
print(len(b))

# result = task6()
# print(result)

# Даны два словаря: dict1= {'a': 300, 'b': 400} и dict2 = {'c': 500, 'd': 600}. Объедините их в один новый словарь.
def task7(dict1, dict2):
    dict3 = {}
    dict3.update(dict1)
    dict3.update(dict2)
    return dict3


d1 = {
    'a': 300,
    'b': 400
}

d2 = {
    'c': 500,
    'd': 600
}

result = task7(d1, d2)
result = task7(d1, {'c': 500})
result = task7(d1, d2)


# print(result)


# Дан словарь с числовыми значениями.
# Например, d = {'a': 12, 'b': 34, 'c': 11}.
# Необходимо найти сумму всех этих значений.
def task8(d):
    sum = 0
    for number in d.values():
         sum = sum + number
         # sum += number
    return sum


print(task8({'a': 12, 'b': 34, 'c': 11}))
print(task8({'a': 12, 'b': 34}))
print(task8({'a': 12}))
print(task8({}))

def task8_2(d):
    value_of_integer = d['a'] + d['b'] + d['c']
    return value_of_integer


x = 2 * task8({'a': 12, 'b': 34, 'c': 11}) + 100 * task8({'a': 12})

print(task8({'a': 12}))


# result = task8()
# print(result)

# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в квадрат,
# то есть {1: 1, 2: 4, 3: 9, ..., 10: 100}

def task9():  # РЕШЕНИЕ ПОЧТИ ПОЛНОСТЬЮ ПОСМОТРЕЛ В ЧАТ ГТП, НАДО БЫЛО НЕМНОГО ДОДУМАТЬ,
    # ШЕЛ В ПРАВИЛЬНОМ НАПРАВЛЕНИИ, НО ТОТАЛ ЗАПИХАЛ НЕ ТУДА, СДЕЛАЛ ЭНЕМЕРЕЙТ ВМЕСТО АЙТЕМС,
    # А ТАК ПОЧТИ-ПОЧТИ, НО НЕ ДО КОНЦА
    num = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10
    }
    total = []
    for index, number in num.items():
        square = number ** 2
        total.append(square)
    return total


# result = task9()
# print(result)

# Даны два словаря. Вывести на экран те ключи, которые есть в обоих словарях.
def task10():
    book_info = {
        'name': 'Martin Iden',
        'author': 'Jack London',
        'publishing': '2012',
        'publisher': 'Binom'
    }
    book_info2 = {
        'name': 'War and Peace',
        'publishing': '1985'
    }
    similar_id = []
    for index in book_info.keys():
        if index in book_info2.keys():
            similar_id.append(index)
    return similar_id


result = task10()
print(result)

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist:
# insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

def task1():
    # Создать словарь, который хранит информацию о книге: название - Мартин Иден, автор - Джек Лондон,
    # год издания - 2012, кол-во страниц - 170, издательство - Бином.
    book = {
        'название': 'Мартин Иден',
        'автор': 'Джек Лондон',
        'год издания': '2012',
        'кол-во страниц': '170',
        'издательство': 'Бином',
    }
    pass


def task2():
    # Создать пустой словарь. Вывести словарь на экран. Добавить значение 2000 с ключом year.
    # Вывести словарь на экран. Добавить значение 'BMW' с ключом model. Вывести словарь на экран.
    # Удалить значение с ключом year. Вывести словарь на экран. Изменить BMW на Audi. Вывести словарь на экран.
    a = {}
    print(a)
    a.update({'year': 5})
    print(a)
    a.update({'model': 'BMW'})
    print(a)
    a.pop('model')
    print(a)
    a.pop('year')
    print(a)
    a.update({'model': 'BMW'})
    a.update({'model': 'Audi'})
    print(a)


def task3():
    # Дан словарь man = {'name': 'Ivan', 'age': 20}. Вывести на экран список ключей, то есть name, age.
    # Вывести на экран список значений, то есть Ivan, 20. Создать копию словаря в переменную person.
    # Очистить исходный словарь man.
    man = {'name': 'Ivan', 'age': 20}
    print(man.keys())
    print(man.get('name'), man.get('age'))
    person = {}
    person = man.copy()
    man.clear()
    print(man, person)


def task4():
    # Дан словарь man = {'name': 'Ivan', 'languages': ['php', 'java', 'python']}.
    # Вывести на экран кол-во языков программирования, которыми владеет Ivan.
    man = {'name': 'Ivan', 'languages': ['php', 'java', 'python']}
    print(man.get('languages'))


def task5():
    # Даны два словаря: dict1= {'a': 300, 'b': 400} и dict2 = {'c': 500, 'd': 600}. Объедините их в один новый словарь.
    dict1 = {'a': 300, 'b': 400}
    dict2 = {'c': 500, 'd': 600}
    dict_new = {}
    dict_new.update(dict1)
    dict_new.update(dict2)
    print(dict_new)


def task6():
    # Дан словарь с числовыми значениями. Например, d = {'a': 12, 'b': 34, 'c': 11}.
    # Необходимо найти сумму всех этих значений.
    d = {'a': 12, 'b': 34, 'c': 11}
    dict_summ = 0

    number = sum(d.values())
    print(number)


def task7():
    # Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в квадрат,
    # то есть {1: 1, 2: 4, 3: 9, ..., 10: 100}
    pass


def task8():
    # Даны два словаря. Вывести на экран те ключи, которые есть в обоих словарях.
    pass

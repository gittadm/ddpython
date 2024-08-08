import random


# Сгенерировать случайное целое число от 10 до 99
def task1():
    return random.randint(10, 99)


result = task1()
print(result)


# Сгенерировать случайное действительное число от 1 до 2
def task2():
    return random.uniform(1, 2)


result = task2()
print(result)


def task3(container, counter, total_summ):
    empty_container = []
    while counter < MAX:
        random_number = random.choice(container)
        empty_container.append(random_number)
        counter += 1
    for number in empty_container:
        total_summ += number
    return f"{empty_container}, TOTAL SUMM = {total_summ}"

counter = 0
total_summ = 0
MAX = 10
empty_container = []
container = list(range(1, 11))
result = task3(container, counter, total_summ)
print(result)


# Сгенерировать случайное четное число от 2 до 20
def task5():
    while True:
        number = random.randint(2, 20)
        if number % 2 == 0:
            return number


result = task5()
print(result)


# Показать случайную дату в виде dd.mm.yyyy Например, 01.02.1994

def task6(day, month, year):
    return f"{random.choice(day):02d}.{random.choice(month):02d}.{random.choice(year)}"


day = list(range(1, 32))
month = list(range(1, 13))
year = list(range(900, 2020))
result = task6(day, month, year)
print(result)


# Показать 10 случайных дат со временем. Например, 01.02.1994 20:24:13
def task7(day, month, year, hour, minute, second):
    return (f"{random.choice(day):02d}.{random.choice(month):02d}.{random.choice(year)}, "
            f"{random.choice(hour):02d}:{random.choice(minute):02d}:{random.choice(second):02d}")


day = list(range(1, 32))
month = list(range(1, 13))
year = list(range(900, 2020))
hour = list(range(1, 13))
minute = list(range(0, 60))
second = list(range(0, 60))
result = task7(day, month, year, hour, minute, second)
print(result)

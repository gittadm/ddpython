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


def task3(container, max=10):
    generated_numbers = []
    counter = 0
    total_summ = 0
    while counter < max:
        random_number = random.choice(container)
        generated_numbers.append(random_number)
        counter += 1
    for number in generated_numbers:
        total_summ += number
    return total_summ


container = list(range(1, 11))
result = task3(container)
print(f"{container}, TOTAL SUMM = {result}")

# СТО
#     кисточка
#     очки
#     форму
#     растворил
#     банку
#
#
# автомобиль
# цвет


# Сгенерировать случайное четное число от 2 до 20
# 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
def task5():
    # 2 способ
    # number = random.randint(1, 10)
    # return 2 * number

    while True:
        number = random.randint(2, 20)
        if number % 2 == 0:
            return number


result = task5()
print(result)


# Показать случайную дату в виде dd.mm.yyyy Например, 01.02.1994

def task6(day, month, year):
    return f"{random.randint(1, 31):02d}.{random.choice(month):02d}.{random.choice(year)}"


day = list(range(1, 32))
month = list(range(1, 13))
year = list(range(900, 2020))
result = task6(day, month, year)
print(result)

def add_zero(k):
    return str(k) if k > 9 else '0' + str(k)

# преждевременная оптимизация зло
# бритва Оккама
def genDate(min_year=1800, max_year=2024):
    year = random.randint(min_year, max_year)
    month = random.randint(1, 12)
    monthDayCounts = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    index = month - 1
    maxDaysCount = monthDayCounts[index]
    day = random.randint(1, maxDaysCount)

    # monthDayCounts = {
    #     'january': 31,
    #     'february': 28,
    # }

    format_day = add_zero(day)
    format_month = add_zero(month)

    return format_day + '.' + format_month + '.' + str(year)

result = genDate(2014)
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

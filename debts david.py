import random


# Сгенерировать 10 квадратных уравнений с целыми коэффициентами, каждое уравнение должно иметь 2 корня.
# То есть сгенерировать целые числа a, b, c - коэффициенты квадратного уравнения так, чтобы дискриминант был больше 0.
def quadratic_eq(count=10):
    equations = []
    while len(equations) < count:
        a = random.randint(-50, 50)
        b = random.randint(-50, 50)
        c = random.randint(-50, 50)
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0 and a != 0:
            equations.append(f'{a}x^2 + ({b}x) + ({c}) = 0')
    return equations


result = quadratic_eq(10)
for equation in result:
    print(equation)

# Сгенерировать список из 10 чисел:
# 7 нулей и 3 единицы. Единицы расположены
# на случайных местах в списке.
def selection(max=10):
    container = []
    while len(container) < max:
        unit = random.randint(0, 1)
        container.append(unit)
        if container.count(1) > 3:
            container[-1] = 0

    return container


result = selection(10)
print(result)


# Дан список школьных предметов.
# Выбрать из него три различных предмета.

def choose_disciplines(disciplines, count=3):
    if count > len(disciplines):
        count = len(disciplines)

    choice = []
    while len(choice) < count:
        unit = random.choice(disciplines)
        if unit not in choice:
            choice.append(unit)

    return choice

# ds = ['math', 'physics', 'chemistry', 'sledding', 'snowball']
# result = choose_disciplines(ds, 3)
# print(result)

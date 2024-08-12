import random

# Дано число n. Генерировать и
# показывать случайные целые числа
# от 1 до 3 до тех пор, пока их сумма меньше n.

def gen_n_number(n=9):
    total = 0
    while total < n:
        unit = random.randint(1, 3)
        print(unit)
        total += unit

    return f'TOTAL = {total}'

result = gen_n_number(9)
print(result)

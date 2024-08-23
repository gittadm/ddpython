# Дан список чисел. Найти наибольшее кол-во подряд идущих нулей в нем. Например, [0, 1, 0, 0, 0, 2, 3, 0, 0] -> 3

def find_zeros(container):
    general_counter = 0
    current_counter = 0
    for number in container:
        if number == 0:
            current_counter += 1
            general_counter = max(current_counter, general_counter)
        elif number != 0:
            current_counter *= 0
    return general_counter


result = find_zeros(container=[0, 1, 0, 0, 0, 2, 3, 0, 0])
print(f'AMOUNT OF ZEROS IS {result}')

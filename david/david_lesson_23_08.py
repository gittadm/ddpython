# Дан список чисел. Выведите все элементы списка,
# каждый из которых больше своего предыдущего элемента.

# [1, 3, 2, 5, 1, 5]
# 3, 5, 5

a = [1999, 30000, 2, 5, 1, 5]
b = []

# index = 3
# print(a[index])

# index = 0 number = 1999 b = []
#     if -
# index = 1 number = 30000
#     if + -> b = [30000]
# index = 2 number = 2
#     if -
# index = 3 number = 5
#     if + -> b = [30000, 5]

for index, number in enumerate(a):
    if index == 0:
        continue
    if a[index] > a[index - 1]:
        b.append(number)

# Показать все числа, каждое из которых равно сумме своих соседних
# то есть слева и справа ближайшие числа (по одному с каждой стороны)
a = [0, 2,  2,     5,    3, 4, 1, 1, 3]
#        index-1 index index+1
# 2 (2 = 0 + 2), 5 (5 = 2 + 3), 4 (4 = 3 + 1)
b = []
for index, number in enumerate(a):
    if index > 0 and index < len(a) - 1 and a[index] == a[index - 1] + a[index + 1]:
        b.append(number)

print(b)

# Дан список чисел. Выведите все наибольшие числа и их индексы.
a = [3, 1, 5, 4, 4, 5, 5]
# 5 - 2
# 5 - 5
# 5 - 6

max_number = max(a)
for index, number in enumerate(a):
    if number == max_number:
        print(max_number, '-', index)

a = [3, 1, 5, 4, 4, 5, 5]
max = a[0]
for number in a:
    if number > max:
        max = number
print('Max number: ', max)


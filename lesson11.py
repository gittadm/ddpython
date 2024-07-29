# список a = [1, 4, 5]  a[1] = 8
# словарь
# кортеж a = (1, 4, 5) - нельзя изменять  tuple
# множество

a = [1, 4, 5]
b = (1, 4, 5)

print(a.__sizeof__())
print(b.__sizeof__())

c = tuple()
d = ()
e = (1, )
e = 1, 2, 3

a = 4
b = 5

b, a = a, b  # поменять местами значения переменных

# c = a
# a = b
# b = c

t = 5, 40, 300
print(t[2])
print(len(t))

# дан кортеж. найти наибольший элемент
def find_max(my_tuple):
    max = my_tuple[0]
    for number in my_tuple:
        if number > max:
            max = number
    return max


print(find_max((5, 4, 30)))

my_tuple = (1, 2, [1, 2, 3])
print(my_tuple[2])
# my_tuple[1] = 4
# my_tuple[2] = [2, 3]
my_tuple[2][0] = 555
print(my_tuple)

# МНОЖЕСТВО
# неупорядоченное
# не может быть повторов
lst = [1, 2, 3, 3]
s = set(lst)
print(s)
s = {3, 3, 3, 3, 5, 6}
print(s)
print(len(s))
x = 5
if x in s:
    print('Yes')
    s.remove(x)
print(s)
s.discard(x)

s = {3, 5, 7, 8}
for number in s:
    print(number)

s2 = s.copy()

s1 = {3, 5, 7, 8}
s2 = {5, 7, 9}

s3 = s1.union(s2)
print(s3)

s4 = s1.intersection(s2)
print(s4)

s1.intersection_update(s2)
print(s1)

s1 = {5, 7}
s2 = {5, 7, 9}

s5 = s1.difference(s2)
print(s5)

s6 = s1.symmetric_difference(s2)
print(s6)

if s1.issubset(s2):
    print('s1 in s2')
else:
    print('no')

basket = {1, 4, 5, 5}
vol = {1, 4, 6}

print(basket.intersection(vol))
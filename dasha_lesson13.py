import random


def get_code(symbol):
    # Дан символ. Показать его код
    code = ord(symbol)
    return code


letter = get_code('N')
print('task1:')
print(letter)


def get_symbol(code):
    # Дан код. Показать символ, соответствующий коду
    result = chr(code)
    return result


code_symbol = get_symbol(78)
print('task2:')
print(code_symbol)


def show_symbol_table(min_number=0, max_number=127):
    # Вывести на экран таблицу символов с кодами (коды от 0 до 127)
    symbol_table = {}

    for x in range(min_number, max_number + 1):
        symbol_table[x] = chr(x)

    return symbol_table


result_table = show_symbol_table()
print('task3')
print(result_table)


def get_phone_number():
    # Сгенерировать случайный номер телефона России. Формат: +7(код)номер, код -
    # задать несколько вариантов (из 3 цифр) в коде и выбирать случайно, номер - 7 цифр.
    code = '+7' + str(random.choice(['(901)', '(956)', '(999)']))
    for x in range(7):
        number = random.randint(0, 9)
        code += str(number)
    return code


phone_number = get_phone_number()
print('task4')
print(phone_number)


# Задание 5. Написать генерацию строк длины 12, первые 5 символов которой - четные цифры,
# следующие 5 символов - буквы 'a' - 'z'
def get_random_string_base(string_length=12):
    even_numbers = [str(x) for x in range(9) if x % 2 == 0]
    small_letters = [chr(x) for x in range(97, 123)]
    symbols = [chr(x) for x in range(33, 48)]

    a = random.choices(even_numbers, k=string_length - 7)
    b = random.choices(symbols, k=string_length - 2 * len(even_numbers))
    c = random.choices(small_letters, k=len(even_numbers))
    random_string = (a, b, c)
    return random_string


def get_password():
    result_password = ''
    for x in range(len(get_random_string_base())):
        result_password += ''.join(get_random_string_base()[x])
    return result_password


generated_password = get_password()
print('task5')
print(generated_password)


# Задание 6. Написать генерация числа от 10000 до 99999, в котором должна быть хотя бы одна цифра 8.
def check_eights(a=10000, b=99999):
    numbers = [x for x in range(a, b + 1)]
    special_numbers = []
    for x in numbers:
        if '8' in str(x):
            special_numbers.append(x)
    return special_numbers


def generate_number_with_eight():
    number_with_eight = random.choice(check_eights())
    return number_with_eight


print('task6')
number_result = generate_number_with_eight()
print(number_result)


# Задание 7. Сгенерировать случайный адрес сайта. Например, www.site.ru - начинается с http, https или www.
# Домен - один из вариантов: ru, by, net, com.
def task7(min_letters=10):
    protocol = random.choice(['http://', 'https://', 'www.'])
    domain = random.choice(['.ru', '.by', '.net', '.com'])
    site_name = random.choices([chr(x) for x in range(97, 123)], k=min_letters)
    return str(protocol) + ''.join(site_name) + str(domain)


result_site_name = task7()
print('task7')
print(result_site_name)


def task8(length=12):
    # Написать генерацию строк длины 12, первые 5 символов которой - четные цифры,
    # следующие 5 символов - буквы 'a' - 'z', следующие 2 символа - "AB",
    # если среди первых пяти символов строки есть цифра 8, "XY"  - если нет.
    even_numbers = [str(x) for x in range(9) if x % 2 == 0]
    small_letters = [chr(x) for x in range(97, 123)]
    a = random.choices(even_numbers, k=length - 7)
    b = random.choices(small_letters, k=len(even_numbers))

    if '8' in a:
        c = 'AB'
    else:
        c = 'XY'

    random_string = [a, b, c]
    result_string = ''

    for x in range(len(random_string)):
        result_string += ''.join(random_string[x])
    return result_string


result_string_2 = task8()
print('task8')
print(result_string_2)


# Задание 9. Написать генерацию строк длины 10, причем первые 4 символа - цифры,
# следующие два символа - различные буквы, следующие 4 символа - нули или единицы,
# причем одна единица точно присутствует.
def task9():
    pass


# Задание 10. Усложнить задачу про генерацию квадратных уравнений: нельзя сократить, корни целые, нет одинаковых.
def task10():
    pass

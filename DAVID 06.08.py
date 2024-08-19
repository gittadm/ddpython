import random


# Компьютер загадывает число от 1 до 100. У пользователя три попытки отгадать.
# После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число. Реализовать игру в консоли.

def pc_make_a_wish():
    return random.randint(1, 100)


def user_guess():
    return int(input('What is your number?: '))


def compare(pc_number):
    tries = 0
    while tries < 3:
        user_number = user_guess()
        tries += 1
        if user_number == pc_number:
            print('Yes')
            break
        elif user_number > pc_number:
            print('more')
        else:
            print('less')


pc_number = pc_make_a_wish()
compare(pc_number)

# Игра. Дано число n. Например, n = 10. Пользователь и компьютер по очереди называют целое число от 1 до 3 до тех пор,
# пока сумма названных чисел меньше n. Как только сумма становится равной n, то игра заканчивается и выигрывает тот,
# кто сделал последний ход, то есть назвал последнее число. Реализовать игру в консоли.

def pc_generate():
    return random.randint(1, 3)


def user_bet():
    return int(input('INPUT: '))


def user_check(user_number):
    while True:
        if user_number < 1 or user_number > 3:
            return False
        return True


def estimation(n=10):

    current_sum = 0
    while current_sum < n:
        computer = pc_generate()
        print(f'\n COMPUTER NUMBER = {computer}')
        user_number = user_bet()
        while not user_check(user_number):
            print('NUMBER CANNOT BE MORE OR LESS THAN 1 OR 3!')
            user_number = user_bet()
        current_sum += computer + user_number
        print(f' TOTAL = {current_sum}')
    defeat_definition(current_sum)

def defeat_definition(current_sum):
    if current_sum > 10:
        print('COMPUTER WINS!')
    else:
        print('USER WINS!')


estimation(10)


# Дан список фамилий. Найти кол-во однофамильцев.
# Например, ['ivanov', 'petrov', 'ivanov', 'petrov', 'ivanov', 'petrov'] - 6,
# ['ivanov', 'petrov', 'ivanov'] - 2, ['ivanov', 'petrov'] - 0

def find_similar_names(names):
    container = []
    for word in names:
        container.append(word)
    return container


def check_similar(names):
    similar_names = find_similar_names(names)
    counter = 0
    for name in similar_names:
        if names.count(name) > 1:
            counter += 1
    return counter


names = ['ivanov', 'petrov', 'ivanov', 'petrov', 'ivanov', 'petrov', 'petrov', 'pepyaka']
result = check_similar(names)
print(result)


# Дан символ. Показать его код

def show_code(symbol):
    return ord(symbol)


symbol = 'A'
result = show_code(symbol)
print(result)

# Дан символ. Показать его код

def show_symbol(code):
    return chr(code)


code = 85
result = show_symbol(code)
print(result)



# Вывести на экран таблицу символов с кодами (коды от 0 до 127)


def transform_into_char(number):
    charity = chr(number)
    return charity


def show_table(numbers):
    result = ''
    for number in numbers:
        charity = transform_into_char(number)
        result += f'Dec = {number}, Char = {charity} \n'
    return result


number = list(range(0, 128))
result = show_table(number)
print(result)



# Сгенерировать случайный номер телефона России. Формат: +7(код)номер, код - задать несколько вариантов (из 3 цифр)
# в коде и выбирать случайно, номер - 7 цифр.


def choose_code_zone(code_zone):
    code_zone = random.choice(code_zone)
    return code_zone


def generate_number():
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    phone_number = []
    length = 0
    while length < 7:
        length += 1
        random_number = random.choice(number_list)
        phone_number.append(random_number)
    return phone_number


def mutate_to_number(prefix, code_zone):
    connection = generate_number()
    connection1 = choose_code_zone(code_zone)
    number = prefix + connection1
    for collect in connection:
        number += str(collect)
    return number


code_zone = ['(705)', '(775)', '(721)']
prefix = '+7'
result = mutate_to_number(prefix, code_zone)
print(result)



# Написать генерацию строк длины 12, первые 5 символов которой - четные цифры, следующие 5 символов - буквы 'a' - 'z'

def generate_numbers(n=5):
    numbers = []
    while len(numbers) < n:
        number = random.randint(0, 255)
        if number % 2 == 0:
            numbers.append(number)
    return numbers


def generate_letters(n=5):
    letters = []
    symbols = list(range(97, 123))
    while len(letters) < n:
        letter = chr(random.choice(symbols))
        letters.append(letter)
    return letters

def mutate_to_string():
    first_piece = generate_numbers()
    second_piece = generate_letters()
    connection = first_piece + second_piece
    return ''.join(map(str, connection))

result = mutate_to_string()
print(result)



# Написать генерация числа от 10000 до 99999, в котором должна быть хотя бы одна цифра 8.

def find_eight(unit1, length):
    container = []
    while len(container) < length:
        unit = random.randint(10000, 99999)
        unit_str = str(unit)
        if str(unit1) in unit_str:
            container.append(unit)
    return container


unit1 = 8
length = 1
result = find_eight(unit1, length)
print(result)

# Сгенерировать случайный адрес сайта.
# Например, www.site.ru - начинается с http, htpps или www. Домен - один из вариантов: ru, by, net, com.

def generate_prefix(prefix):
    return random.choice(prefix)


def generate_postfix(postfix):
    return random.choice(postfix)


def generate_address(n=12):
    address = []
    while len(address) < n:
        charity = chr(random.randint(97, 122))
        address.append(charity)
    return ''.join(address)


def mutate_to_website(prefix, postfix):
    connection = generate_prefix(prefix)
    address = generate_address(n=12)
    connection2 = generate_postfix(postfix)
    website = f'{connection}://{address}.{connection2}'
    return website


prefix = ['http', 'https']
postfix = ['ru', 'by', 'net', 'com']
n = 12
result = mutate_to_website(prefix, postfix)
print(result)

# Написать генерацию строк длины 12, первые 5 символов которой - четные цифры, следующие 5 символов - буквы 'a' - 'z',
# следующие 2 символа - "AB", если среди первых пяти символов строки есть цифра 8, "XY"  - если нет.

def generate_number(n=5):
    number_container = []
    while len(number_container) < n:
        numbers = random.randint(0, 16)
        if numbers % 2 == 0:
            number_container.append(str(numbers))
    return ''.join(number_container)


def generate_charity(n=5):
    charity_container = []
    while len(charity_container) < n:
        charity = chr(random.randint(97, 122))
        charity_container.append(charity)
    return ''.join(charity_container)


def mutate_to_smth():
    connection = generate_number(n=5)
    connection_1 = generate_charity(n=5)
    smth = connection + connection_1
    for collection in connection:
        if '8' not in collection:
            return f'{smth}AB'
        else:
            return f'{smth}XY'


result = mutate_to_smth()
print(result)



# Написать генерацию строк длины 10, причем первые 4 символа - цифры, следующие два символа -
# различные буквы, следующие 4 символа - нули или единицы, причем одна единица точно присутствует.

def generate_numbers(n):
    number_container = []
    while len(number_container) < n:
        number = random.randint(0, 5)
        number_container.append(str(number))
    return ''.join(number_container)


def generate_letters(n_1):
    letters = (
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    letter_container = []
    while len(letter_container) < n_1:
        a_b = random.choice(letters)
        letter_container.append(a_b)
    return ''.join(letter_container)


def generate_zeros_and_ones(n_2):
    zeros_and_ones_container = []
    while len(zeros_and_ones_container) < n_2:
        zeros_and_ones = random.randint(0, 1)
        zeros_and_ones_container.append(str(zeros_and_ones))
    return ''.join(zeros_and_ones_container)

def unite():
    connection_0 = generate_numbers(n)
    connection_1 = generate_letters(n_1)
    connection_2 = generate_zeros_and_ones(n_2)
    united_elements = f'{connection_0}{connection_1}{connection_2}'
    return united_elements


n = 4
n_1 = 2
n_2 = 4
result = unite()
print(result)

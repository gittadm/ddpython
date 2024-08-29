import random

# random.seed(1)

# print(random.randint(1, 10))
# print(random.choice([1, 3, 6, 8]))
# print(random.uniform(1, 5))
#
# x = random.randint(1, 10)
# y = x + 1
#
# print(y)

# Сгенерировать 3 различных
# случайных целых числа
# от 1 до 10
def gen():
    min = 1
    max = 10

    a = random.randint(min, max)

    b = random.randint(min, max)
    while b == a:
        b = random.randint(min, max)

    c = random.randint(min, max)
    while c == a or c == b:
        c = random.randint(min, max)

    print(a, b, c)

def gen2():
    min = 1
    max = 10

    a = random.randint(min, max)

    if a == max:
        max = a - 1
    else:
        min = a + 1

    b = random.randint(min, max)

    print(a, b)

# Камень, ножницы, бумага с компьютером
# 10 игр. И статистика и кто победил.

def is_user_win(user, computer):
    return (user == 'к' and computer == 'н') or (user == 'н' and computer == 'б') or (user == 'б' and computer == 'к')

def game():
    game_number = 1
    user_wins = 0
    computer_wins = 0
    # games = [
    #     {'user': 'k', 'computer': 'k'},
    #     {'user': 'н', 'computer': 'k'},
    #     {'user': 'k', 'computer': 'б'},
    #     {'user': 'k', 'computer': 'k'},
    # ]
    # print(games[2]['computer'])  # 'б'
    games = []
    while game_number <= 10:
        user = input('Ваш ход (к, н, б): ')
        computer = random.choice(['к', 'н', 'б'])
        games.append({'user': user, 'computer': computer});
        if is_user_win(user, computer):
            user_wins += 1
        elif user != computer:
            computer_wins += 1

        game_number += 1

    if user_wins == computer_wins:
        print('ничья')
    elif user_wins > computer_wins:
        print('пользователь выиграл')
    else:
        print('компьютер выиграл')

    print(games)

# game()

games = [3, 5, 7, 3]
games[2] = 8

a = {'name': 'ivan', 'age': 20}
a['age'] = 30

games = [
    {'name': 'ivan', 'age': 20},
    {'name': 'ivan', 'age': 20},
    {'name': 'ivan', 'age': 22},
    {'name': 'ivan', 'age': 20},
]

print(games[2]['age'])
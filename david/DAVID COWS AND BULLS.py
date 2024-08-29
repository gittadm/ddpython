import random


# Игра Быки и Коровы. Компьютер загадывает трехзначное число. Пользователь угадывает число.
# После каждой попытки компьютер сообщает пользователю, сколько цифр совпало, причем на правильных местах, (быки)
# и сколько цифр есть в загаданном числе, но они стоят на неправильных местах в числе пользователя (коровы).

def generation_pc(n=4):
    computer = []
    while len(computer) < n:
        pc_came_up = random.randint(0, 9)
        computer.append(pc_came_up)
        if pc_came_up not in computer:
            computer.append(pc_came_up)
    return computer


def guess_player(n=4):
    while True:
        player_input = list(map(int, input('Mooo! Write 4-digits number: ')))
        if len(player_input) == n and len(set(player_input)) == n:
            return player_input
        else:
            print("Please enter 4 unique digits.")


def bulls_and_cows(computer, player):
    bulls = 0
    cows = 0
    for index, number in enumerate(player):
        if number == computer[index]:
            bulls += 1
        elif number in computer:
            cows += 1
    return bulls, cows


def unite(n=4):
    computer = generation_pc(n=4)
    player = guess_player(n=4)
    bulls, cows = bulls_and_cows(player, computer)
    print(f'{bulls} bulls, {cows} cows')

    while bulls < n:
        player = guess_player(n=4)
        bulls, cows = bulls_and_cows(player, computer)
        print(f'{bulls} bulls, {cows} cows')

    print("Congratulations! You've guessed the number correctly.")


unite()
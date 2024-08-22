import random


def generation_pc(n=4):
    computer = []
    while len(computer) < n:
        pc_came_up = random.randint(0, 9)
        if pc_came_up not in computer:
            computer.append(pc_came_up)
    return computer


def guess_player(n=4):
    while True:
        player_input = list(map(int, input('Mooo! Write a 4-digit number: ')))
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


def result():
    computer = generation_pc(n=4)
    player = guess_player(n=4)
    bulls, cows = bulls_and_cows(computer, player)
    print(f'{bulls} быков, {cows} коров')


result()

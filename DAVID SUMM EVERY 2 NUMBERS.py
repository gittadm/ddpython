import random


def generate_number(n=4):
    container = []
    while len(container) < n:
        unit = random.randint(0, 9)
        container.append(unit)
    return container


def calculate_number(container):
    new_container = []
    for index in range(len(container)):
        if index < len(container) - 1:
            new_sum = container[index] + container[index + 1]
            new_container.append(new_sum)
    return new_container


def add_number():
    unit = generate_number(n=4)
    unit1 = calculate_number(unit)  # Исправлено с 'container' на 'unit'
    final_container = []
    counter = 0
    for index, number in enumerate(unit):
        final_container.append(number)
        counter += 1
        if counter >= 2:
            final_container.append(unit1[counter - 2])  # Исправлено на append вместо insert
            counter -= 2
    return final_container


container = generate_number()
result = calculate_number(container)
add = add_number()

print("Generated container:", container)
print("Calculated result:", result)
print("Final added numbers:", add)

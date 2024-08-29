# def calculate(a):
#     return 2 * a + 8
#
# def show():
#     print(2)
#
# a = [1, 2, 3]
# max_number = max(a)
#
# calculate(5)
# calculate(10)
# calculate(15)

# Найти наибольшее число из двух данных чисел
def find_max(b, d, a=9, c=6):
    if a > b:
        return a

    return b


x = (find_max(2, 88) + 2) * find_max(4, 1) + find_max(1, 2)
print(x)

# Список [4, 8, 3]
# Словарь

# Клиент name, year, price, description, phone
# client = ['Petr', 1990, 123, 'не курит', '+799912312312']

client = {
    'name': 'Petr',
    'year': 1990,
    'price': 123,
    'description': 'не курит',
    'phone': '+799912312312',
}

client['year'] += 10

# print(client['price'])

#print(client)

for key in client:
    print(key, client[key])

print(list(client.values()))
print(list(client.keys()))

clients = [
    {
        'name': 'Petr',
        'year': 1990,
        'price': 17,
        'description': 'не курит',
        'phone': '+799912312312',
    },
    {
        'name': 'Alex',
        'year': 1999,
        'price': 123,
        'description': 'не курит',
        'phone': '+799912312312',
    },
    {
        'name': 'Ivan',
        'year': 2000,
        'price': 12,
        'description': 'не курит',
        'phone': '+799912312312',
    },
]

print(clients[0]['price'])

total_price = 0
for client in clients:
    total_price += client['price']

print('Total price:', total_price)

client = {
    'name': 'Ivan',
    'year': 2000,
}

client.update({'price': 5, 'year': 1990})
client['year'] = 2020
client['description'] = 'yes'

del client['year']

print(client)


def find_young_client_name(clients):
    max_year = clients[0]['year']
    client_index = 0

    for index, client in enumerate(clients):
        if client['year'] > max_year:
            max_year = client['year']
            client_index = index

    return clients[client_index]['name']

print(find_young_client_name(clients))

client = {
    'name': 'Ivan',
    'year': 2000,
}

# print(client['description'])
print(client.get('description', 'No data'))

client2 = client.copy()

client['name'] = 'Petr'
print(client2)


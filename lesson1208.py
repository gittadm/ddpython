import random

# сгенерировать случайные пароли:
# 1) кол-во символов от 8 до 15
# 2) цифры, англ буквы, спецсимволы _!@#$%^&

def gen_password(n = 10):
    code = ord('a')  # 97
    code = ord('z')  # 122
    code = random.randint(97, 122)
    char = chr(code)
    print(char)

    s = ''
    length = random.randint(8, 15)
    for i in range(length):
        # 97 - 122 a-z
        # 65 - 90  A-Z
        # 48 - 57  0 - 9
        # 33 - 38, 95 _!@#$%^&

        letter_code = random.randint(97, 122)
        up_letter_code = random.randint(65, 90)
        digit_code = random.randint(48, 57)
        spec_symbols_code = random.randint(33, 38)
        spec_symbol_code = 95

        codes = []
        for i in range(97, 123):
            codes.append(i)
        for i in range(65, 91):
            codes.append(i)
        # ...

        code = random.choice(codes)

        # code = random.choice([letter_code, up_letter_code, digit_code, spec_symbol_code, spec_symbols_code])

        s += chr(code)

        codes = list(range(97, 123))
        codes += list(range(65, 91))

        symbol = chr(random.choice(codes))
        s += symbol
        print(codes)

    print(s)

gen_password()
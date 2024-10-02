import random

from string import ascii_lowercase, ascii_uppercase, digits, punctuation


all_symbols = ascii_lowercase + ascii_uppercase + digits + punctuation

'''
ascii_lowercase - abcdefghijklmnopqrstuvwxyz
ascii_uppercase - ABCDEFGHIJKLMNOPQRSTUVWXYZ
digits          - 0123456789
punctuation     - !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''
sym_dict = {
    '1': ascii_lowercase,
    '2': ascii_uppercase,
    '3': digits,
    '4': punctuation
}


def password():
    print(
        '\npassword generator > available characters:\n',
        f'1) lower: {ascii_lowercase}',
        f'2) upper: {ascii_uppercase}',
        f'3) numbers: {digits}',
        f'4) symbols: {punctuation}',
        sep='\n'
    )
    user_input = input('\nenter which characters to use, '
                       'separated by a space (default=all):\n').split(' ')
    
    symbols = ''
    try:
        for i in user_input:
            symbols += sym_dict[i]
    except:
        print('characters: default\n')
        symbols = all_symbols
    
    try:
        length = int(input('enter the password length (default=16):\n'))
        print()
    except:
        print('length: default\n')
        length = 16
    
    password = ''.join(random.sample(symbols, length))
    print(f'password: {password}')

if __name__ == '__main__':
    password()
    input('\npress ENTER to close')
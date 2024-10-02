import random

from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation
)



all_symbols = ascii_lowercase + ascii_uppercase + digits + punctuation

passwd_dict = {
    1: ascii_lowercase,
    2: ascii_uppercase,
    3: digits,
    4: punctuation
}



def gen_passwd():
    print(
        '\nPassword generator.\nAvailable characters:\n',
        f'1) {passwd_dict[1]}',
        f'2) {passwd_dict[2]}',
        f'3) {passwd_dict[3]}',
        f'4) {passwd_dict[4]}',
        sep='\n'
    )
    chars = input('\nEnter which characters to use, '
                  'separated by a space (default=[1 2 3]): ').strip()
    
    user_chars = map(int, chars.split(' '))
    symbols = ''
    
    if chars:
        for i in user_chars:
            symbols += passwd_dict[i]
    else:
        print('Characters: default')
        symbols += f'{passwd_dict[1]}{passwd_dict[2]}{passwd_dict[3]}'
    
    try:
        length = int(input(
            '\nEnter the password length (default=16): ').strip())
    except ValueError:
        print('Length: default')
        length = 16
    
    password = ''.join(random.sample(symbols, length))
    print(f'\nPassword: {password}\n')

if __name__ == '__main__':
    gen_passwd()
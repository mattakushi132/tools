'''
Unit          Abbreviation Equivalent in bytes

1.  bit       b            1
2.  byte      B            8 bits
3.  kilobyte  KB           1024 bytes
4.  megabyte  MB           1024 kilobytes
5.  gigabyte  GB           1024 megabytes
6.  terabyte  TB           1024 gigabytes
7.  petabyte  PB           1024 terabytes
8.  exabyte   EB           1024 petabytes
9.  zettabyte ZB           1024 exabytes
10. yottabyte YB           1024 zettabytes
'''


def byte_to_kilobyte(byte):
    return byte / 1024
def byte_to_megabyte(byte):
    return (byte / 1024) / 1024
def byte_to_gigabyte(byte):
    return ((byte / 1024) / 1024) / 1024
def byte_to_terabyte(byte):
    return (((byte / 1024) / 1024) / 1024) / 1024

def kilobyte_to_byte(kilobyte):
    return kilobyte * 1024
def kilobyte_to_megabyte(kilobyte):
    return kilobyte / 1024
def kilobyte_to_gigabyte(kilobyte):
    return (kilobyte / 1024) / 1024
def kilobyte_to_terabyte(kilobyte):
    return ((kilobyte / 1024) / 1024) / 1024

def megabyte_to_byte(megabyte):
    return (megabyte * 1024) * 1024
def megabyte_to_kilobyte(megabyte):
    return megabyte * 1024
def megabyte_to_gigabyte(megabyte):
    return megabyte / 1024
def megabyte_to_terabyte(megabyte):
    return (megabyte / 1024) / 1024

def gigabyte_to_byte(gigabyte):
    return ((gigabyte * 1024) * 1024) * 1024
def gigabyte_to_kilobyte(gigabyte):
    return (gigabyte * 1024) * 1024
def gigabyte_to_megabyte(gigabyte):
    return gigabyte * 1024
def gigabyte_to_terabyte(gigabyte):
    return gigabyte / 1024

def terabyte_to_byte(terabyte):
    return (((terabyte * 1024) * 1024) * 1024) * 1024
def terabyte_to_kilobyte(terabyte):
    return ((terabyte * 1024) * 1024) * 1024
def terabyte_to_megabyte(terabyte):
    return (terabyte * 1024) * 1024
def terabyte_to_gigabyte(terabyte):
    return terabyte * 1024


def converter():
    print(
        '\nunit converter:\n',
        'byte (b)',
        'kilobyte (kb)',
        'megabyte (mb)',
        'gigabyte (gb)',
        'terabyte (tb)',
        '\nexample: "500 gb>mb"\n',
        sep='\n'
    )
    action = input('> ')
    value, unit = map(str, action.split(' '))
    value = int(value)
    print()
    
    if unit == 'b>kb':
        print(f'> {byte_to_kilobyte(value)} KB')
    elif unit == 'b>mb':
        print(f'> {byte_to_megabyte(value)} MB')
    elif unit == 'b>gb':
        print(f'> {byte_to_gigabyte(value)} GB')
    elif unit == 'b>tb':
        print(f'> {byte_to_terabyte(value)} TB')
    
    elif unit == 'kb>b':
        print(f'> {kilobyte_to_byte(value)} B')
    elif unit == 'kb>mb':
        print(f'> {kilobyte_to_megabyte(value)} MB')
    elif unit == 'kb>gb':
        print(f'> {kilobyte_to_gigabyte(value)} GB')
    elif unit == 'kb>tb':
        print(f'> {kilobyte_to_terabyte(value)} TB')
    
    elif unit == 'mb>b':
        print(f'> {megabyte_to_byte(value)} B')
    elif unit == 'mb>kb':
        print(f'> {megabyte_to_kilobyte(value)} KB')
    elif unit == 'mb>gb':
        print(f'> {megabyte_to_gigabyte(value)} GB')
    elif unit == 'mb>tb':
        print(f'> {megabyte_to_terabyte(value)} TB')
    
    elif unit == 'gb>b':
        print(f'> {gigabyte_to_byte(value)} B')
    elif unit == 'gb>kb':
        print(f'> {gigabyte_to_kilobyte(value)} KB')
    elif unit == 'gb>mb':
        print(f'> {gigabyte_to_megabyte(value)} MB')
    elif unit == 'gb>tb':
        print(f'> {gigabyte_to_terabyte(value)} TB')
    
    elif unit == 'tb>b':
        print(f'> {terabyte_to_byte(value)} B')
    elif unit == 'tb>kb':
        print(f'> {terabyte_to_kilobyte(value)} KB')
    elif unit == 'tb>mb':
        print(f'> {terabyte_to_megabyte(value)} MB')
    elif unit == 'tb>gb':
        print(f'> {terabyte_to_gigabyte(value)} GB')


if __name__ == '__main__':
    converter()
    input('\npress ENTER to close')



'''
Предложения по улучшению от нейросети:
    1) Добавить типизацию функций и проверку входных данных на корректность.
    2) Упростить логику конвертации с помощью дополнительных функций и констант.
    3) Добавить комментарии и документацию к функциям.
    4) Улучшить пользовательский интерфейс консольной утилиты.
'''
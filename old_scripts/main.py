'''
Commands and PopuGAY
'''
# python modules:
import random

# my scripts:
from calculator import calc
from color_converter import color_converter
from current_time import ctm
from cursor_info import main_cursor
from examples import math_examples
from password_generator import password
from tiny_url import short_url
from unit_converter import converter
from qr_creator import qr_create
from working_with_files import files

parrot = 'PopuGAY'  # parrot - попугай
randNum = random.randint


def popugay():
    print(f'\n{parrot}: helou! \t(type "help" for help)\n')
    
    command = str(input('-> ')).lower().strip()
    
    if command == 'help':
        print(
            '\ncommand list:\n',
            '1) rand (randomizer)',
            '2) calc (calculator)',
            '3) exams (mathematical examples)',
            '4) curs (interactions with the cursor)',
            '5) time (current time)',
            '6) color (color converter)',
            '7) unit (unit converter)',
            '8) passwd (password generator)',
            '9) url (url shortening)',
            '10) qr (qr creator)',
            '11) files (working with files)',
            '12) ...',
            '13) ...',
            '14) ...',
            '\nif you enter something other than a command, '
            'the PopuGAY will repeat it '
            '(or respond with something else...).\n',
            sep='\n'
        )
        command = str(input('-> ')).lower().strip()
    
    if command in ['1', 'rand']:
        rNum1, rNum2 = map(int, input('\n"Num1 Num2": ').split(' '))
        print(f'\n{parrot}: {randNum(rNum1,rNum2)}')
    
    elif command in ['2', 'calc']: calc()
    elif command in ['3', 'exams']: math_examples()
    elif command in ['4', 'curs']: main_cursor()
    elif command in ['5', 'time']: ctm()
    elif command in ['6', 'color']: color_converter()
    elif command in ['7', 'unit']: converter()
    elif command in ['8', 'passwd']: password()
    elif command in ['9', 'url']: short_url()
    elif command in ['10', 'qr']: qr_create()
    elif command in ['11', 'files']: files()
    
    elif command in ['12']: print('\nComing soon! (or not soon...)')
    elif command in ['13']: print('\nComing soon! (or not soon...)')
    elif command in ['14']: print('\nComing soon! (or not soon...)')
    
    elif command in ['dungeon']: print(f'\n{parrot}: master...')
    else: print(f'\n{parrot}: {command}')

if __name__ == '__main__':
    popugay()
    input('\npress ENTER to close')
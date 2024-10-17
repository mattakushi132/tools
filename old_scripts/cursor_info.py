import sys
import pyautogui


class cursor:
    def position():
        while True:
            try:
                x, y = pyautogui.position()
                sys.stdout.write(f'\rX:{x}  Y:{y}        ')
                sys.stdout.flush()
            except KeyboardInterrupt:
                break
    
    def rgb():
        while True:
            try:
                x, y = pyautogui.position()
                sys.stdout.write(f'\rRGB:{pyautogui.pixel(x, y)}        ')
                sys.stdout.flush()
            except KeyboardInterrupt:
                break

def main_cursor():
    print(
        '\nchoose what to read:\n',
        '1) coordinates',
        '2) rgb\n',
        sep='\n'
    )
    choice = str(input('-> '))
    
    if choice == '1':
        print()
        cursor.position()

    elif choice == '2':
        print()
        cursor.rgb()

if __name__ == '__main__':
    main_cursor()
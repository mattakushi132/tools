def hex_to_rgb(hex_color):
    """
    Преобразует строку в формате HEX в кортеж из трех целых чисел,
    представляющих значения красного, зеленого и синего компонентов цвета.
    """
    hex_color = hex_color.lstrip('#')  # Убираем символ '#' из начала строки
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in range(0,
                                                               len(hex_color),
                                                               2))
    return rgb_color

# """ сложна.. НЕПОНЯТНА... """
# def rgb_to_hex(rgb_tuple):
#     r, g, b = rgb_tuple
#     return '#{:02x}{:02x}{:02x}'.format(r,g,b)

def rgb_to_hex(rgb_color):
    """
    Преобразует строку в формате "R,G,B" в строку в формате HEX,
    представляющую цвет в шестнадцатеричном формате.
    """
    r, g, b = map(int, rgb_color.split(','))
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

def color_converter():
    print(
        '\nconvert:\n',
        '1) hex to rgb',
        '2) rgb to hex',
        sep='\n'
    )
    
    choice = input('\n> ')
    
    if choice == '1':
        color = input('\nhex: ')
        print(f'rgb: {hex_to_rgb(color)}')
    
    elif choice == '2':
        color = input('\n"r,g,b": ')
        print(f'hex: {rgb_to_hex(color)}')

if __name__ == '__main__':
    color_converter()
    input('\npress ENTER to close')
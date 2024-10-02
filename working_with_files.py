def file_management(way, txt=''):
    file_location = 'example.txt'
    
    if way == 'read':
        with open(f'files/{file_location}', 'r') as file_1:
            print(f'\nthe contents of the file "{file_location}":\n')
            print(file_1.read())
    
    elif way == 'write':
        with open(f'files/{file_location}', 'w') as file_1:
            file_1.write(txt)
            print(f'\nthe data was written to the file "{file_location}"')

def files():
    print(
        '\nworking with files:\n',
        '1) read',
        '2) write',
        '3) ...',
        sep='\n'
    )
    act = str(input('\n> ')).lower().strip()
    
    if act in ['1', 'read']:
        file_management(way='read')
    
    elif act in ['2', 'write']:
        text = input('\nenter what will be written to the file:\n\n')
        file_management(way='write', txt=text)

if __name__ == '__main__':
    files()
    input('\npress ENTER to close')
'''
QR(Quick Response) codes - Коды быстрого реагирования
'''
import pyqrcode


def qr_create():
    qr_str = str(input('\nURL: '))
    png_name = str(input('qr_"name".png: '))
    
    if (qr_str != '') and (png_name != ''):
        url_to_qr = pyqrcode.create(qr_str)
        url_to_qr.png(f'files/qr_{png_name}.png', scale=8)
        
        print(f'\n"qr_{png_name}.png" successfully created')
    
    else: print('\nThe fields should not be empty!')

if __name__ == '__main__':
    qr_create()
    input('\npress ENTER to close')
import pyshorteners


def short_url():
    pys = pyshorteners.Shortener()
    tiny_url = pys.tinyurl.short(input('\nurl: '))
    
    print(f'\ntiny url: {tiny_url}\n')

if __name__ == '__main__':
    short_url()
    input('\npress ENTER to close')
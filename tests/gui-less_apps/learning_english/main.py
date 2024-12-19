'''
Learning English:
'''
from learn_words import learning_words
from learn_glossary import learning_glossary



def main():
    print(
        '\nEnglish..\n',
        '  Learning:\n',
        '1) Words (default)',
        '2) Glossary',
        '3) Soon...',
        '4) Soon...',
        sep='\n',
        end='\n\n'
    )
    user_input = input('> ').lower().strip()
    
    match user_input:
        case '1' | '': learning_words()
        case '2': learning_glossary()
        case '3': print('\nComing soon! (or not soon...)')
        case '4': print('\nComing soon! (or not soon...)')
        case _: print('\n?>.<?')

if __name__ == '__main__':
    try:
        main()
        input('\npress ENTER to close')
    except KeyboardInterrupt:
        print('KeyboardInterrupt\n')
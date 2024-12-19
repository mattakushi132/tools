'''
Words update (english/files/dictionary.json):

Functions:
    update_dict
    set_errors
'''
import re
import json
from random import randint



def old_dict() -> dict:
    """
    Returns:
        dict: from "english/files/dictionary.json" if it exist
    """
    try:
        with open(dict_json, encoding='utf-8') as dj:
            data = json.load(dj)
    except FileNotFoundError as e:
        print(f'FileNotFoundError: {e}')
        data = {}
    except json.decoder.JSONDecodeError as e:
        print(f'json.decoder.JSONDecodeError: {e}')
        data = {}
    return data

def new_dict() -> dict:
    """
    Returns:
        dict: created from the "english/files/words.txt" file
    Example:
        {"words": [{"en": ["word_1"], "ru": ["Слово_1", "Слово_2"]}, {...}]}
    """
    with open(words_txt, encoding='utf-8') as wt:
        words = [x.replace('\n', '') for x in wt.readlines() if x != '\n']
    
    dictionary = {'words': []}
    
    for w in words:
        en_words, ru_words = w.split(' - ')
        
        if re.search(', ', en_words):
            en = en_words.split(', ')
        else:
            en = [en_words]
        
        if re.search(', ', ru_words):
            ru = ru_words.split(', ')
        else:
            ru = [ru_words]
        
        dictionary['words'].append({
            'en': en,
            'ru': ru
        })
    else:
        with open(dict_words, 'w', encoding='utf-8') as d:
            json.dump(dictionary, d, ensure_ascii=False, indent=4)
    
    return dictionary

def update_dict() -> None:
    """
    Update dictionary words:
        "english/files/dictionary.json"
    """
    try:
        old_dict_words = old_dict()['words']
    except KeyError as e:
        print(f'KeyError: {e}')
        od = old_dict()
        od['words'] = []
        old_dict_words = od['words']
    
    new_dict_words = new_dict()['words']
    updated_dict = old_dict().copy()
    
    try:
        updated_dict_words = updated_dict['words'] = []
    except KeyError:
        updated_dict['words'] = []
        updated_dict_words = updated_dict['words']
    
    for i in range(len(new_dict_words)):
        try:
            updated_dict_words.append({
                'en': new_dict_words[i]['en'],
                'ru': new_dict_words[i]['ru'],
                'errors': {
                    'en': old_dict_words[i]['errors']['en'],
                    'ru': old_dict_words[i]['errors']['ru']
                }
            })
        except IndexError:
            updated_dict_words.append({
                'en': new_dict_words[i]['en'],
                'ru': new_dict_words[i]['ru'],
                'errors': {
                    'en': 0,
                    'ru': 0
                }
            })
    else:
        with open(dict_json, 'w', encoding='utf-8') as ud:
            json.dump(updated_dict, ud, ensure_ascii=False, indent=4)
        
        print('\nThe dictionary has been updated',
              '(some data may have been lost)')

def set_errors(way: str = 'clear') -> None:
    """
    Args:
        way (str, optional): Clear/set words errors. Defaults to 'clear'.
    """
    try:
        _old_dict = old_dict()
        old_dict_words = _old_dict['words']
    except KeyError as e:
        print(f'KeyError: {e}')
    else:
        for words in old_dict_words:
            num_1 = 0 if way == 'clear' else randint(0, len(old_dict_words))
            num_2 = 0 if way == 'clear' else randint(0, len(old_dict_words))
            
            words['errors'] = {'en': num_1, 'ru': num_2}
        else:
            with open(dict_json, 'w', encoding='utf-8') as od:
                json.dump(_old_dict, od, ensure_ascii=False, indent=4)
            
            if way == 'clear':
                print('\nThe dictionary has been cleared.')
            else:
                print(f'\nSet random errors: 0-{len(old_dict_words)}')

if __name__ == '__main__':
    dict_words = 'dict_words.json'
    dict_json = '../files/dictionary.json'
    words_txt = '../files/words.txt'
else:
    dict_words = 'other/dict_words.json'
    dict_json = 'files/dictionary.json'
    words_txt = 'files/words.txt'
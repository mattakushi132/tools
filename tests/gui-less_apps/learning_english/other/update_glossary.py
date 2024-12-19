'''
Glossary update (english/files/dictionary.json):

Functions:
    update_dict
    set_errors
'''
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
        dict: created from the "english/files/glossary.txt" file
    Example:
        {"glossary": [{"Keys": "Words"}, {...}]}
    """
    with open(glossary_txt, encoding='utf-8') as gt:
        glossary = [x.replace('\n', '') for x in gt.readlines() if x != '\n']
    
    dictionary = {'glossary': []}
    
    for i in glossary:
        if i == '-':
            counter = 0
            glossary_dict = {}
        else:
            counter += 1
            
            if counter == 1:  # Полное предложение
                glossary_dict['en_full'] = i
            elif counter == 2:  # Предложение со скрытым главным словом
                glossary_dict['en_part'] = i
            elif counter == 3:  # Главное слово
                glossary_dict['en_word'] = i
            elif counter == 4:  # ...
                glossary_dict['ru_full'] = i
            elif counter == 5:  # ...
                glossary_dict['ru_part'] = i
            elif counter == 6:  # ...
                glossary_dict['ru_word'] = i
                dictionary['glossary'].append(glossary_dict)
    else:
        with open(dict_glossary, 'w', encoding='utf-8') as d:
            json.dump(dictionary, d, ensure_ascii=False, indent=4)
    
    return dictionary

def update_dict() -> None:
    """
    Update dictionary glossary:
        "english/files/dictionary.json"
    """
    try:
        old_dict_glossary = old_dict()['glossary']
    except KeyError as e:
        print(f'KeyError: {e}')
        od = old_dict()
        od['glossary'] = []
        old_dict_glossary = od['glossary']
    
    new_dict_glossary = new_dict()['glossary']
    updated_dict = old_dict().copy()
    
    try:
        updated_dict_glossary = updated_dict['glossary'] = []
    except KeyError:
        updated_dict['glossary'] = []
        updated_dict_glossary = updated_dict['glossary']
    
    for i in range(len(new_dict_glossary)):
        try:
            updated_dict_glossary.append({
                'en_full': new_dict_glossary[i]['en_full'],
                'en_part': new_dict_glossary[i]['en_part'],
                'en_word': new_dict_glossary[i]['en_word'],
                'ru_full': new_dict_glossary[i]['ru_full'],
                'ru_part': new_dict_glossary[i]['ru_part'],
                'ru_word': new_dict_glossary[i]['ru_word'],
                'errors': {
                    'en': old_dict_glossary[i]['errors']['en'],
                    'ru': old_dict_glossary[i]['errors']['ru'],
                }
            })
        except IndexError:
            updated_dict_glossary.append({
                'en_full': new_dict_glossary[i]['en_full'],
                'en_part': new_dict_glossary[i]['en_part'],
                'en_word': new_dict_glossary[i]['en_word'],
                'ru_full': new_dict_glossary[i]['ru_full'],
                'ru_part': new_dict_glossary[i]['ru_part'],
                'ru_word': new_dict_glossary[i]['ru_word'],
                'errors': {
                    'en': 0,
                    'ru': 0,
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
        way (str, optional): Clear/set glossary errors. Defaults to 'clear'.
    """
    try:
        _old_dict = old_dict()
        old_dict_glossary = _old_dict['glossary']
    except KeyError as e:
        print(f'KeyError: {e}')
    else:
        for glossary in old_dict_glossary:
            if way == 'clear':
                num_1, num_2 = 0, 0
            else:
                num_1 = randint(0, len(old_dict_glossary))
                num_2 = randint(0, len(old_dict_glossary))
            
            glossary['errors'] = {
                'en': num_1,
                'ru': num_2,
            }
        else:
            with open(dict_json, 'w', encoding='utf-8') as od:
                json.dump(_old_dict, od, ensure_ascii=False, indent=4)
            
            if way == 'clear':
                print('\nThe dictionary has been cleared.')
            else:
                print(f'\nSet random errors: 0-{len(old_dict_glossary)}')

if __name__ == '__main__':
    dict_glossary = 'dict_glossary.json'
    dict_json = '../files/dictionary.json'
    glossary_txt = '../files/glossary.txt'
else:
    dict_glossary = 'other/dict_glossary.json'
    dict_json = 'files/dictionary.json'
    glossary_txt = 'files/glossary.txt'
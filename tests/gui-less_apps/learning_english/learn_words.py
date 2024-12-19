import random
import re
import json

from other.update_words import update_dict, set_errors



with open('files/dictionary.json', encoding='utf-8') as d:
    dictionary = json.load(d)
    dict_words = dictionary['words']

def get_index_list_errors(lang='en', top=10):
    unsorted_errors_list = [i['errors'][lang] for i in dict_words]
    sorted_errors_list = sorted(enumerate(unsorted_errors_list),
                                key=lambda x: x[1], reverse=True)
    
    errors_index_list = []
    for index, errors in sorted_errors_list[:top]:
        if errors != 0:
            errors_index_list.append(index)
        else:
            break
    
    return errors_index_list

def print_top_errors(from_to='en>ru', top=10):
    from_lang, to_lang = from_to.split('>')
    
    errors_index_list = get_index_list_errors(to_lang, top)
    
    if len(errors_index_list) < 1:
        print('\nThere is no progress.')
    elif len(errors_index_list) < top:
        print("\nIt looks like you've just started learning English,",
              f"here are your {len(errors_index_list)} errors:\n")
    else:
        if to_lang == 'en':
            print(f'\nTop {top} errors from Russian to English:\n')
        else:
            print(f'\nTop {top} errors from English to Russian:\n')
    
    counter = 0
    for i in errors_index_list:
        counter += 1
        print(f'\n{counter})'
              f' {", ".join(dict_words[i][from_lang]).capitalize()}'
              f' - {", ".join(dict_words[i][to_lang]).capitalize()}'
              f'     ({dict_words[i]['errors'][to_lang]})')
    if errors_index_list: print()

def words(way='en>ru'):
    if re.search('>', way):
        from_lang, to_lang = way.split('>')
    else:
        from_lang, to_lang = 'en', 'ru'
    
    EXIT = ['/', '/EXIT', '/QUIT']
    EXIT_MSG = 'Enter "/" to finish'
    
    index_list = list(range(len(dict_words)))
    errors_list = []
    
    right_answers = 0
    wrong_answers = 0
    counter = 0
    
    top_en_errors = get_index_list_errors('en', 15)
    top_ru_errors = get_index_list_errors('ru', 15)
    
    while True:
        counter += 1
        
        if way == 'alternately':
            from_lang, to_lang = to_lang, from_lang
        elif way == 'random':
            if random.randint(0, 1):
                from_lang, to_lang = 'en', 'ru'
            else:
                from_lang, to_lang = 'ru', 'en'
        
        if to_lang == 'en' and top_en_errors:
            index = random.choice(top_en_errors)
            top_en_errors.remove(index)
            
            if index in top_ru_errors:
                top_ru_errors.remove(index)
        elif to_lang == 'ru' and top_ru_errors:
            index = random.choice(top_ru_errors)
            top_ru_errors.remove(index)
            
            if index in top_en_errors:
                top_en_errors.remove(index)
        elif index_list:
            index = random.choice(index_list)
        else:
            break
        
        # Всё ещё выходит "ValueError: list.remove(x): x not in list" (редко)...
        index_list.remove(index)
        
        from_lang_words = dict_words[index][from_lang]
        to_lang_words = dict_words[index][to_lang]
        
        print('\n\n{0:_>10} / [{2}] / {1:_<10} {3}'.format(right_answers,
                                                           wrong_answers,
                                                           counter, EXIT_MSG))
        print(f'\n{", ".join(from_lang_words).capitalize()}\n')
        
        user_input = input('> ').lower().strip().replace('ё', 'е')
        
        if user_input in to_lang_words:
            print('\n\nRIGHT!')
            right_answers += 1
            
            if len(to_lang_words) > 1:
                other_meanings = [x for x in to_lang_words if x != user_input]
                print('And it also means: '
                      f'{", ".join(other_meanings).capitalize()}.')
        elif user_input.upper() in EXIT:
            break
        else:
            print('\n\nWRONG!\n\nRight answer(-s):',
                  f'{", ".join(to_lang_words).capitalize()}.')
            
            wrong_answers += 1
            dict_words[index]['errors'][to_lang] += 1
            
            errors_list.append({
                'from': from_lang_words,
                'to': to_lang_words,
                'user_answer': user_input if user_input else '-',
                
                'index': index,
                'to_lang': to_lang,
                'not_displayed': True,
            })
        
        wrong_words = [x for x in errors_list if x['not_displayed']]
        
        if (wrong_words
                and len(errors_list) >= 30
                and random.randint(0, 19) == 0):
            wrong_word = random.choice(wrong_words)
            
            print('\n\n{0:_^30} {1}\n'.format('Repetition', EXIT_MSG))
            print(
                f'{", ".join(wrong_word['from']).capitalize()}'
                f' - {", ".join(wrong_word['to']).capitalize()}'
                '\n\nYour answer: '
                f'{wrong_word['user_answer'].capitalize()}'
            )
            wrong_word['not_displayed'] = False
            
            if input('\n\nNEXT? ').upper() in EXIT:
                break
        
        if (wrong_words
                and len(errors_list) >= 30
                and random.randint(0, 49) == 0):
            wrong_word = random.choice(wrong_words)
            
            print('\n\n{0:_^30} {1}\n'.format('!!! Repetition !!!', EXIT_MSG))
            print(f'{", ".join(wrong_word['from']).capitalize()}\n')
            
            user_input = input('> ').lower().strip().replace('ё', 'е')
            
            if user_input in wrong_word['to']:
                print('\n\nRIGHT!')
                
                ww_index = wrong_word['index']
                ww_lang = wrong_word['to_lang']
                
                dict_words[ww_index]['errors'][ww_lang] -= 1
                
                if len(wrong_word['to']) > 1:
                    other_means = []
                    
                    for i in wrong_word['to']:
                        if i != user_input:
                            other_means.append(i)
                    
                    print('And it also means: '
                          f'{", ".join(other_means).capitalize()}.')
            elif user_input.upper() in EXIT:
                break
            else:
                print("\n\nAlas, even this time you didn't give"
                      " the right answer.")
                print('\nRight answer(-s): '
                      f'{", ".join(wrong_word['to']).capitalize()}.')
            
            wrong_word['not_displayed'] = False
    
    with open('files/dictionary.json', 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)
    
    print('\n\n_____ The test is completed _____\n')
    
    r_space = ' ' * (len('right') - len(str(right_answers)))
    w_space = ' ' * (len('wrong') - len(str(wrong_answers)))
    score = right_answers - wrong_answers
    
    print('Answers:',
          'Right - Wrong = Score',
          f'{right_answers}{r_space} - {wrong_answers}{w_space} = {score}',
          sep='\n',
          end='\n\n')
    
    if errors_list:
        question = f'Do you want to repeat wrong({len(errors_list)}) answers?'
        repeat = input(f'{question} (+/-): ').lower().strip()
        
        if repeat in ['+', 'y', 'yes']:
            repeat_counter = 0
            answer_attempts = 0
            answer_skips = 0
            
            print()
            for e in errors_list:
                repeat_counter += 1
                
                if e['user_answer'] != '-':
                    answer_attempts += 1
                else:
                    answer_skips += 1
                
                print(f'\n{repeat_counter})'
                      f' {", ".join(e['from']).capitalize()}'
                      f' - {", ".join(e['to']).capitalize()}'
                      f'     ({e['user_answer']})')
            else:
                print('\n\nAttempts to Answer | Skips\n'
                      '{0: >18} | {1: <5}\n'.format(answer_attempts,
                                                    answer_skips))

def learning_words():
    print(
        '\nLearning Words:\n',
        '1) En -> Ru',
        '2) Ru -> En',
        '3) Alternately',
        '4) Random (default)',
        '\n5) Top 10 English errors',
        '6) Top 10 Russian errors',
        '\n7) Number of Words',
        '8) Update dictionary',
        '\n9) Clear errors',
        '10) Set random errors',
        sep='\n',
        end='\n\n'
    )
    user_input = input('> ').lower().strip()
    
    match user_input:
        case '1': words('en>ru')
        case '2': words('ru>en')
        case '3' | 'alt': words('alternately')
        case '4' | 'rand' | '': words('random')
        case '5': print_top_errors('ru>en')
        case '6': print_top_errors('en>ru')
        case '7': print(f'\nWords: {len(dict_words)}')
        case '8': update_dict()
        case '9' | 'clear': set_errors('clear')
        case '10': set_errors('random')
        case _: print('\n?>.<?')

if __name__ == '__main__':
    try:
        learning_words()
        input('\npress ENTER to close')
    except KeyboardInterrupt:
        print('KeyboardInterrupt\n')
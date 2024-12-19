import random
import re
import json

from other.update_glossary import update_dict, set_errors



with open('files/dictionary.json', encoding='utf-8') as d:
    dictionary = json.load(d)
    dict_glossary = dictionary['glossary']

def get_index_list_errors(lang='en', top=10) -> list:
    unsorted_errors_list = [x['errors'][lang] for x in dict_glossary]
    sorted_errors_list = sorted(enumerate(unsorted_errors_list),
                                key=lambda x: x[1], reverse=True)
    
    errors_index_list = []
    for index, errors in sorted_errors_list[:top]:
        if errors != 0:
            errors_index_list.append(index)
        else:
            break
    
    return errors_index_list

def print_top_errors(to_lang='en', top=10):
    errors_index_list = get_index_list_errors(to_lang, top)
    
    if len(errors_index_list) == top:
        if to_lang == 'en':
            from_lang = 'ru'
            print(f'\nTop {top} English errors:')
        else:
            from_lang = 'en'
            print(f'\nTop {top} Russian errors:')
        
        counter = 0
        for i in errors_index_list:
            counter += 1
            
            print(f'\n{counter}) '
                  f'{dict_glossary[i][f'{to_lang}_word'].capitalize()}...\n'
                  f'{dict_glossary[i][f'{to_lang}_part']}\n\n'
                  f'{dict_glossary[i][f'{from_lang}_full']}\n')
    else:
        print(f'\nThere is no progress or it is less than {top}.')

def glossary(way='en'):
    if re.search('>', way):
        from_lang, to_lang = way.split('>')
    else:
        if way == 'en':
            from_lang, to_lang = 'ru', 'en'
        else:
            from_lang, to_lang = 'en', 'ru'
    
    EXIT = ['/', '/EXIT', '/QUIT']
    EXIT_MSG = 'Enter "/" to finish'
    
    possible_answers = ['1', '2', '3', '4', '']
    
    index_list = list(range(len(dict_glossary)))
    en_errors_indexes = get_index_list_errors('en', 15)
    ru_errors_indexes = get_index_list_errors('ru', 15)
    errors_list = []
    
    right_answers = 0
    wrong_answers = 0
    counter = 0
    
    while True:
        counter += 1
        
        if to_lang == 'en' and en_errors_indexes:
            index = random.choice(en_errors_indexes)
            en_errors_indexes.remove(index)
            
            if index in ru_errors_indexes:
                ru_errors_indexes.remove(index)
        elif to_lang == 'ru' and ru_errors_indexes:
            index = random.choice(ru_errors_indexes)
            ru_errors_indexes.remove(index)
            
            if index in en_errors_indexes:
                en_errors_indexes.remove(index)
        elif index_list:
            index = random.choice(index_list)
        else:
            break
        
        index_list.remove(index)
        
        print('\n\n{0:_>10} / [{2}] / {1:_<10} {3}'.format(right_answers,
                                                           wrong_answers,
                                                           counter, EXIT_MSG))
        
        if re.search('>', way):
            print("\n\nIt's not finished\n")
            break
        else:
            part_term = dict_glossary[index][f'{to_lang}_part']
            word_term = dict_glossary[index][f'{to_lang}_word']
            
            print(f'\n{part_term}\n')
            
            other_word_terms = [word_term]
            while len(other_word_terms) < 4:
                rand_term = dict_glossary[
                    random.randint(0, len(dict_glossary)-1)
                ]
                rand_word_term = rand_term[f'{to_lang}_word']
                
                if rand_word_term not in other_word_terms:
                    other_word_terms.append(rand_word_term)
            else:
                random.shuffle(other_word_terms)
            
            other_word_terms_dict = {}
            for i in range(4):
                other_word_terms_dict[str(i+1)] = other_word_terms[i]
            
            for key, value in other_word_terms_dict.items():
                print(f'{key}) {value.capitalize()}')
                
                if value == word_term:
                    right_answer = key
            
            while True:
                user_input = str(input('\n> ').lower().strip())
                
                if (user_input in possible_answers) or (user_input in EXIT):
                    break
                else:
                    print("\nThat doesn't seem like a possible answer")
            
            if user_input == right_answer:
                right_answers += 1
                print('\nRight!')
            elif user_input.upper() in EXIT:
                break
            else:
                wrong_answers += 1
                dict_glossary[index]['errors'][to_lang] += 1
                print(f'\nWrong!\nRight answer: {right_answer}')
                
                if user_input in possible_answers:
                    if user_input == '':
                        user_answer = '-'
                    else:
                        user_answer = other_word_terms_dict[user_input]
                
                errors_list.append({
                    'term': part_term,
                    'right_answer': word_term,
                    'user_answer': user_answer,
                })
    
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
            
            for e in errors_list:
                repeat_counter += 1
                
                print(
                    f'\n{repeat_counter}) '
                    f'{e['right_answer'].capitalize()}...\n{e['term']}'
                    f'\nYour answer: "{e['user_answer'].capitalize()}"'
                )

def learning_glossary():
    print(
        '\nLearning Glossary terms:\n',
        '\nThe output of the part of the term with 4 possible answers:',
        '1) En (default)',
        '2) Ru',
        '\nThe output of the term and 4 possible answers '
            'in another language:',
        '3) (soon...) En -> Ru',
        '4) (soon...) Ru -> En',
        '\nOther:',
        '5) Top 10 English errors',
        '6) Top 10 Russian errors',
        '\n7) Number of Glossary terms',
        '8) Update dictionary',
        '\n9) Clear errors',
        '10) Set random errors',
        sep='\n',
        end='\n\n'
    )
    user_input = input('> ').lower().strip()
    
    match user_input:
        case '1' | '': glossary('en')
        case '2': glossary('ru')
        case '3': print('\nComing soon! (or not soon...)')
        case '4': print('\nComing soon! (or not soon...)')
        case '5': print_top_errors('en')
        case '6': print_top_errors('ru')
        case '7': print(f'\nTerms: {len(dict_glossary)}')
        case '8': update_dict()
        case '9': set_errors('clear')
        case '10': set_errors('random')
        case _: print('\n?>.<?')

if __name__ == '__main__':
    try:
        learning_glossary()
        input('\npress ENTER to close')
    except KeyboardInterrupt:
        print('KeyboardInterrupt\n')
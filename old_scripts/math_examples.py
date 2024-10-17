import random


randNum = random.randint


class Examples:
    def addition():
        correct_answers = 0
        incorrect_answers = 0
        while True:
            num1 = randNum(1,1000)
            num2 = randNum(1,1000)
            result = num1 + num2
            print(f'\n_____ addition ___ '
                  f'({correct_answers} / {incorrect_answers}) _____')
            print(f'\n{num1} + {num2} = ', end='')
            user_input = input('')
            if user_input.lower() in ['exit','quit','']:
                break
            if int(user_input) == result:
                print('the answer is correct!')
                correct_answers += 1
            else:
                print('the answer is wrong!')
                incorrect_answers += 1
                print(f'right answer: {result}')
    
    def subtraction():
        correct_answers = 0
        incorrect_answers = 0
        while True:
            num1 = randNum(1,1000)
            num2 = randNum(1,1000)
            result = num1 - num2
            print(f'\n_____ subtraction ___ '
                  f'({correct_answers} / {incorrect_answers}) _____')
            print(f'\n{num1} - {num2} = ', end='')
            user_input = input('')
            if user_input.lower() in ['exit','quit','']:
                break
            if int(user_input) == result:
                print('the answer is correct!')
                correct_answers += 1
            else:
                print('the answer is wrong!')
                incorrect_answers += 1
                print(f'right answer: {result}')

    def addition_subtraction():
        correct_answers = 0
        incorrect_answers = 0
        while True:
            randOp = randNum(1,2)
            if randOp == 1:
                num1 = randNum(1,1000)
                num2 = randNum(1,1000)
                result = num1 + num2
                print(f'\n_____ addition ___ '
                      f'({correct_answers} / {incorrect_answers}) _____')
                print(f'\n{num1} + {num2} = ', end='')
                user_input = input('')
                if user_input.lower() in ['exit','quit','']:
                    break
                if int(user_input) == result:
                    print('the answer is correct!')
                    correct_answers += 1
                else:
                    print('the answer is wrong!')
                    incorrect_answers += 1
                    print(f'right answer: {result}')
            
            elif randOp == 2:
                num1 = randNum(1,1000)
                num2 = randNum(1,1000)
                result = num1 - num2
                print(f'\n_____ subtraction ___ '
                      f'({correct_answers} / {incorrect_answers}) _____')
                print(f'\n{num1} - {num2} = ', end='')
                user_input = input('')
                if user_input.lower() in ['exit','quit','']:
                    break
                if int(user_input) == result:
                    print('the answer is correct!')
                    correct_answers += 1
                else:
                    print('the answer is wrong!')
                    incorrect_answers += 1
                    print(f'right answer: {result}')

    def multiplication():
        correct_answers = 0
        incorrect_answers = 0
        while True:
            num1 = randNum(2,24)
            num2 = randNum(2,24)
            result = num1 * num2
            print(f'\n_____ multiplication ___ '
                  f'({correct_answers} / {incorrect_answers}) _____')
            print(f'\n{num1} * {num2} = ', end='')
            user_input = input('')
            if user_input.lower() in ['exit','quit','']:
                break
            if int(user_input) == result:
                print('the answer is correct!')
                correct_answers += 1
            else:
                print('the answer is wrong!')
                incorrect_answers += 1
                print(f'right answer: {result}')
    
    def all_at_once():
        correct_answers = 0
        incorrect_answers = 0
        while True:
            randOp = randNum(1,3)
            if randOp == 1:
                num1 = randNum(1,1000)
                num2 = randNum(1,1000)
                result = num1 + num2
                print(f'\n_____ addition ___ '
                      f'({correct_answers} / {incorrect_answers}) _____')
                print(f'\n{num1} + {num2} = ', end='')
                user_input = input('')
                if user_input.lower() in ['exit','quit','']:
                    break
                if int(user_input) == result:
                    print('the answer is correct!')
                    correct_answers += 1
                else:
                    print('the answer is wrong!')
                    incorrect_answers += 1
                    print(f'right answer: {result}')
            
            elif randOp == 2:
                num1 = randNum(1,1000)
                num2 = randNum(1,1000)
                result = num1 - num2
                print(f'\n_____ subtraction ___ '
                      f'({correct_answers} / {incorrect_answers}) _____')
                print(f'\n{num1} - {num2} = ', end='')
                user_input = input('')
                if user_input.lower() in ['exit','quit','']:
                    break
                if int(user_input) == result:
                    print('the answer is correct!')
                    correct_answers += 1
                else:
                    print('the answer is wrong!')
                    incorrect_answers += 1
                    print(f'right answer: {result}')
            
            elif randOp == 3:
                num1 = randNum(2,24)
                num2 = randNum(2,24)
                result = num1 * num2
                print(f'\n_____ multiplication ___ '
                      f'({correct_answers} / {incorrect_answers}) _____')
                print(f'\n{num1} * {num2} = ', end='')
                user_input = input('')
                if user_input.lower() in ['exit','quit','']:
                    break
                if int(user_input) == result:
                    print('the answer is correct!')
                    correct_answers += 1
                else:
                    print('the answer is wrong!')
                    incorrect_answers += 1
                    print(f'right answer: {result}')

def math_examples():
    print(
        '\n1) addition',
        '2) subtraction',
        '3) addition + subtraction',
        '4) multiplication',
        '5) all at once',
        sep='\n'
    )
    user_input = input("\nenter the number: ")
    
    if   user_input == '1': Examples.addition()
    elif user_input == '2': Examples.subtraction()
    elif user_input == '3': Examples.addition_subtraction()
    elif user_input == '4': Examples.multiplication()
    elif user_input == '5': Examples.all_at_once()
    
    else: print('waht>?')

if __name__ == '__main__':
    math_examples()
    input('\npress ENTER to close')
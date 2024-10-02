def calc():
    while True:
        num1, op, num2 = map(str,
                             input('\n"Num1 Operator Num2": ').split(' '))
        num1 = float(num1)
        num2 = float(num2)
        supported_ops = {'+', '-', '*', '/', '**', '//', '%'}
        
        if op not in supported_ops:
            print(f'\nError: Invalid operator "{op}". '
                  f'Supported operators are {" or ".join(supported_ops)}.')
        else:
            match op:
                case '+':
                    result = num1 + num2
                case '-':
                    result = num1 - num2
                case '*':
                    result = num1 * num2
                case '/':
                    try:
                        result = num1 / num2
                    except ZeroDivisionError as e:
                        result = f'error: {e}'
                case '**':
                    result = num1 ** num2
                case '//':
                    try:
                        result = num1 // num2
                    except ZeroDivisionError as e:
                        result = f'error: {e}'
                case '%':
                    result = num1 % num2
        
        print(f'\n= {result}')

def calc_2():  # ...=-=...
    while True:
        try:
            result = eval(input('\n> '))
        except ZeroDivisionError:
            print('\nZeroDivisionError')
            result = 0
        finally:
            print(f'\n= {result}')

if __name__ == '__main__':
    # calc()
    calc_2()
    print('\npress ENTER to close')
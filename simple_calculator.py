import operator

ops = {"+": operator.add, "-": operator.sub, '*': operator.mul, '/': operator.truediv, '%': operator.mod,
       '^': operator.xor, }


def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False


def operation():
    i = 3
    while True:
        operation_input = input('Enter an operation: ')
        i = i - 1
        if operation_input == '+' or operation_input == '-' or operation_input == '*' or operation_input == '/' or operation_input == '%' or operation_input == '^':
            return cal(operation_input)
        elif i <= 0:
            print('Your failed try again')
            break
        print('Invalid sign try again, remaining attempts: ', i)


def cal(operation):
    i = 3
    while True:
        i = i - 1
        number_2 = input('Enter another number: ')
        if isfloat(number_2):
            number_2 = int(number_2)
            result = ops[operation](number_1, number_2)
            print('Result', result)
            print('Lets go on')
            break
        elif i <= 0:
            print('Your failed try again')
            break
        print('Invalid number try again, remaining attempts: ',i)


while True:
    number_1 = input('Enter number (or a letter to exit): ')
    if isfloat(number_1):
        number_1 = int(number_1)
        operation()
    else:
        print('Bye Bye')
        break

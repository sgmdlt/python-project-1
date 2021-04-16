import operator
import random

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def game_calc():
    '''
    Display arithmetic expression and return its result

    Return:
    expression -- string in the format 'first_number sign second_number',
    where first_number, sign, second_number are chosen at random. (ex. '3 + 8')
    correct_answer -- result of chosen expression in 'str' format. (ex. '11')
    '''

    print('What is the result of the expression?')
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)
    (sign, op) = random.choice(list(operators.items()))

    expression = '{first} {s} {second} = '.format(
        first=first_number, s=sign, second=second_number)
    correct_answer = str(op(first_number, second_number))
    return expression, correct_answer

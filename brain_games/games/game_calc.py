import operator
import random

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}
RAND_MIN = 1
RAND_MAX = 20
GAME_MESSAGE = 'What is the result of the expression?'


def game_task():
    '''
    Display arithmetic expression and return its result

    Return:
    expression -- string in the format 'first_number sign second_number',
    where first_number, sign, second_number are chosen at random. (ex. '3 + 8')
    correct_answer -- result of chosen expression in 'str' format. (ex. '11')
    '''

    first_number = random.randint(RAND_MIN, RAND_MAX)
    second_number = random.randint(RAND_MIN, RAND_MAX)
    (sign, op) = random.choice(list(OPERATORS.items()))

    expression = '{first} {s} {second} = '.format(
        first=first_number, s=sign, second=second_number)
    correct_answer = str(op(first_number, second_number))
    return expression, correct_answer

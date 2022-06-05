import operator
import random

OPERATORS = {  # noqa: WPS407
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}
RAND_MIN = 1
RAND_MAX = 20
GAME_MESSAGE = 'What is the result of the question?'


def calculate(op, first_number, second_number):
    operation = OPERATORS.get(op)
    return operation(first_number, second_number)


def game_task():  # noqa: WPS210
    """Display arithmetic question and return its result.

    Return:
    question -- string in the format 'first_number sign second_number',
    where first_number, sign, second_number are chosen at random. (ex. '3 + 8')
    correct_answer -- result of chosen question in 'str' format. (ex. '11')
    """
    first_number = random.randint(RAND_MIN, RAND_MAX)
    second_number = random.randint(RAND_MIN, RAND_MAX)
    sign = random.choice(list(OPERATORS))

    question = f'{first_number} {sign} {second_number} = '
    correct_answer = str(calculate(sign, first_number, second_number))
    return question, correct_answer

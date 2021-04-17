import random


RAND_MIN = 1
RAND_MAX = 20
GAME_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_task():
    '''
    Display random number and return its parity

    Return
    expression -- chosen at random number. (ex. '12')
    correct_ansewr -- 'yes' or 'no' depending on parity (ex. 'yes')
    '''

    expression = random.randint(RAND_MIN, RAND_MAX)
    if expression % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return expression, correct_answer

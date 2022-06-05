import random

RAND_MIN = 1
RAND_MAX = 20
GAME_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def game_task():
    """Display random number and return its parity.

    Return
    number -- chosen at random number. (ex. '12')
    correct_ansewr -- 'yes' or 'no' depending on parity (ex. 'yes')
    """
    number = random.randint(RAND_MIN, RAND_MAX)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer

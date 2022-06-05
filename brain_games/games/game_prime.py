import random

RAND_MIN = 1
RAND_MAX = 20
GAME_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            return False
    return True


def game_task():
    """Display random number and return its primality.

    Return
    question -- random number. (ex. 17)
    correct_answer -- 'yes' if number is prime, otherwise 'no'. (ex. 'yes')
    """
    number = random.randint(RAND_MIN, RAND_MAX)
    question = f'{number}'
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

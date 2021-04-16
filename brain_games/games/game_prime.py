import random

PRIME_NUMBERS = (2, 3, 5, 7, 11, 13, 17, 19)
RAND_MIN = 1
RAND_MAX = 20


def game_prime():
    '''
    Display random number and return its primality

    Return
    expression -- random number. (ex. 17)
    correct_answer -- 'yes' if number is prime, otherwise 'no'. (ex. 'yes')
    '''

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    random_number = random.randint(RAND_MIN, RAND_MAX)
    expression = '{n}'.format(n=random_number)
    if random_number in PRIME_NUMBERS:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return expression, correct_answer

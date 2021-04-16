import random


RAND_MIN = 1
RAND_MAX = 10


def find_gcd(first_number, second_number):
    '''Find GCD of two numbers with Euclidean division algorithm'''
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return first_number


def game_gcd():
    '''
    Display two random numbers and return their GCD.

    Return
    expression -- string with two random numbers. (ex. '42 30')
    correct_answer -- their GCD in 'str' format. (ex. '6')
    '''

    print('Find the greatest common divisor of given numbers.')

    base_divisor = random.randint(RAND_MIN, RAND_MAX)
    first_number = base_divisor * random.randint(RAND_MIN, RAND_MAX)
    second_number = base_divisor * random.randint(RAND_MIN, RAND_MAX)
    expression = '{0} {1}'.format(first_number, second_number)

    gcd = find_gcd(first_number, second_number)
    correct_answer = str(gcd)

    return expression, correct_answer

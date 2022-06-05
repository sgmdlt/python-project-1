import random

RAND_MIN = 1
RAND_MAX = 10
GAME_MESSAGE = 'Find the greatest common divisor of given numbers.'


def find_gcd(first_number, second_number):
    """Find GCD of two numbers with Euclidean division algorithm."""
    while first_number != second_number:
        if first_number > second_number:
            first_number -= second_number
        else:
            second_number -= first_number
    return first_number


def game_task():
    """Display two random numbers and return their GCD.

    Return
    question -- string with two random numbers. (ex. '42 30')
    correct_answer -- their GCD in 'str' format. (ex. '6')
    """
    base_divisor = random.randint(RAND_MIN, RAND_MAX)
    first_number = base_divisor * random.randint(RAND_MIN, RAND_MAX)
    second_number = base_divisor * random.randint(RAND_MIN, RAND_MAX)

    question = f'{first_number} {second_number}'
    correct_answer = str(find_gcd(first_number, second_number))

    return question, correct_answer

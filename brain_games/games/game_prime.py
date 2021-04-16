import random

prime_numbers = (2, 3, 5, 7, 11, 13, 17, 19)


def game_prime():
    '''
    Display random number and return its primality

    Return
    expression -- random number. (ex. 17)
    correct_answer -- 'yes' if number is prime, otherwise 'no'. (ex. 'yes')
    '''

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    random_number = random.randint(1, 20)
    expression = '{n}'.format(n=random_number)
    if random_number in prime_numbers:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return expression, correct_answer

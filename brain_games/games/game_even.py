import random


def game_even():
    '''
    Display random number and return its parity

    Return
    expression -- chosen at random number. (ex. '12')
    correct_ansewr -- 'yes' or 'no' depending on parity (ex. 'yes')
    '''

    print('Answer "yes" if the number is even, otherwise answer "no".')
    expression = random.randint(1, 16)
    if expression % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return expression, correct_answer


if __name__ == '__main__':
    game_even()

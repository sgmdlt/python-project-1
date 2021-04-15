import random


def get_prog():
    '''Return start, end and step of random arithmetic progression.'''
    start = random.randint(1, 16)
    step = random.randint(2, 10)
    lenght = random.randint(6, 12)
    end = start + lenght * step
    return start, end, step


def game_progression():
    '''
    Display arithmetic progression and return number in it.

    Return
    expression -- string with progression
    and '...' symbols instead randomly chosen number. (ex. '2 4 ... 8')
    correct_answer -- hidden with '...' number in progression. (ex. '6')
    '''

    print('What number is missing in the progression?')
    prog_string = ' '
    (start, end, step) = get_prog()

    progression = range(start, end, step)
    hidden_number = random.choice(list(progression))

    for number in list(progression):
        if number != hidden_number:
            prog_string += '{num}'.format(num=number) + ' '
        else:
            prog_string += '...' + ' '

    expression = prog_string
    corect_answer = str(hidden_number)
    return expression, corect_answer

import random

START_MIN = 1
START_MAX = 20
STEP_MIN = 2
STEP_MAX = 10
LEN_MIN = 6
LEN_MAX = 12
GAME_MESSAGE = 'What number is missing in the progression?'


def get_prog():
    '''Return start, end and step of random arithmetic progression.'''
    start = random.randint(START_MIN, START_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    lenght = random.randint(LEN_MIN, LEN_MAX)
    end = start + lenght * step
    return start, end, step


def game_task():
    '''
    Display arithmetic progression and return number in it.

    Return
    expression -- string with progression
    and '...' symbols instead randomly chosen number. (ex. '2 4 ... 8')
    correct_answer -- hidden with '..' number in progression. (ex. '6')
    '''

    prog_string = ' '
    (start, end, step) = get_prog()

    progression = range(start, end, step)
    hidden_number = random.choice(list(progression))

    for number in list(progression):
        if number != hidden_number:
            prog_string += '{num}'.format(num=number) + ' '
        else:
            prog_string += '..' + ' '

    expression = prog_string
    corect_answer = str(hidden_number)
    return expression, corect_answer

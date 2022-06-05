import random

START_MIN = 1
START_MAX = 20
STEP_MIN = 2
STEP_MAX = 10
LEN_MIN = 6
LEN_MAX = 12
FILLER = '..'
GAME_MESSAGE = 'What number is missing in the progression?'


def get_progression(start, step, lenght):
    """Return start, end and step of random arithmetic progression."""
    end = start + step * lenght
    return list(range(start, end, step))


def game_task():  # noqa: WPS210
    """Display arithmetic progression and return number in it.

    Return
    question -- string with progression
    and '..' symbols instead randomly chosen number. (ex. '2 4 .. 8')
    correct_answer -- hidden with '..' number in progression. (ex. '6')
    """
    start = random.randint(START_MIN, START_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    lenght = random.randint(LEN_MIN, LEN_MAX)

    prog_list = get_progression(start, step, lenght)
    hidden_number = random.choice(prog_list)

    question = ' '.join(
        str(num) if num != hidden_number else FILLER  # noqa: WPS504
        for num in prog_list
    )
    corect_answer = str(hidden_number)
    return question, corect_answer

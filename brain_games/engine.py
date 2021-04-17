import prompt
from brain_games.welcome import welcome

TRIES = 3


def engine(game_name):
    '''
    Run chosen game and display dialog messages.

    Arguments
    game_name -- name of game module (in 'games' package)
    '''

    user_name = welcome()
    print(game_name.GAME_MESSAGE)
    for _ in range(0, TRIES):
        (expression, correct_answer) = game_name.game_task()
        print('Question: {}'.format(expression))
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was "{}"'
                  .format(user_answer, correct_answer))
            print("Let's try again, {}!".format(user_name))
            return
    print('Congratulations, {}!'.format(user_name))

#!/usr/bin/env python
import prompt


def engine(game_name, user_name):
    for tries in range(0, 3):
        (expression, correct_answer) = game_name()
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

#!/usr/bin/env python
import prompt
import random


def game_even(name):
    # name = welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    tries = 0
    while tries < 3:
        random_number = random.randint(1, 16)
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question: {}'.format(random_number))
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was "{}"'
                  .format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return

        tries += 1

    print('Congratulations, {}!'.format(name))

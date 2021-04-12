#!/usr/bin/env python
import random


def game_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    expression = random.randint(1, 16)
    if expression % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return expression, correct_answer


if __name__ == "__main__":
    game_even()

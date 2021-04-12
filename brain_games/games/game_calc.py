#!/usr/bin/env python
import operator
import random

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def game_calc():
    print('What is the result of the expression?')
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)
    (sign, op) = random.choice(list(operators.items()))
    expression = '{} {} {} = '.format(first_number, sign, second_number)
    correct_answer = str(op(first_number, second_number))
    return expression, correct_answer

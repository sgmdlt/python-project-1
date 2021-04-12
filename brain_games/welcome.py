#!/usr/bin/env python
import prompt


def welcome():
    print('Welcome to Brain Games!')
    user_name = prompt.string('May I have your name?\n')
    print('Hello, {}!'.format(user_name))
    return user_name

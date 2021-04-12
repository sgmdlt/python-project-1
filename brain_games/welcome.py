#!/usr/bin/env python
import prompt


def welcome():
    name = prompt.string('May I have your name?\n')
    print('Hello, {}!'.format(name))
    return name

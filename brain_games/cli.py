#!/usr/bin/env python
import prompt


def welcome_user():
    name = prompt.string('May I have your name?\n')
    print(f'Hello, {name}!')

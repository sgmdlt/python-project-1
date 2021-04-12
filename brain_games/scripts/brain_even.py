#!/usr/bin/env python
from brain_games.game_even import game_even
from brain_games.welcome import welcome


def greet():
    print('Welcome to Brain Games!')


def main():
    greet()
    name = welcome()
    game_even(name)


if __name__ == '__main__':
    main()

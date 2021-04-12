#!/usr/bin/env python
from brain_games.games.game_calc import game_calc
from brain_games.welcome import welcome
from brain_games.scripts.engine import engine


def greet():
    print('Welcome to Brain Games!')


def main():
    greet()
    user_name = welcome()
    engine(game_calc, user_name)


if __name__ == '__main__':
    main()

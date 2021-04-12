#!/usr/bin/env python
from brain_games.games.game_even import game_even
from brain_games.welcome import welcome
from brain_games.scripts.engine import engine


def main():
    user_name = welcome()
    engine(game_even, user_name)


if __name__ == '__main__':
    main()

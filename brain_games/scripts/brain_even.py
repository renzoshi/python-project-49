#!/usr/bin/env/python

from brain_games.game_logic import launch_game
from brain_games.games import game_even


def main():
    launch_game(game_even)


if __name__ == '__main__':
    main()

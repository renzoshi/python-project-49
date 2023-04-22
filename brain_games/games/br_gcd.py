from random import randint
from math import gcd


RULES = 'Find the greatest common divisor of given numbers.'
START_LIMIT = 1
FINISH_LIMIT = 100


def get_start_game():
    rand_num1 = randint(START_LIMIT, FINISH_LIMIT)
    rand_num2 = randint(START_LIMIT, 100)
    question = str(rand_num1) + ' ' + str(rand_num2)
    right_answer = str(gcd(rand_num1, rand_num2))
    return question, right_answer

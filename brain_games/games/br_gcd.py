from random import randint
from math import gcd

RULES = 'Find the greatest common divisor of given numbers.'


def pass_game():
    rand_num1 = randint(1, 100)
    rand_num2 = randint(1, 100)
    ques = str(rand_num1) + ' ' + str(rand_num2)
    right_answer = str(gcd(rand_num1, rand_num2))
    return ques, right_answer

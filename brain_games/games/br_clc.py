from random import randint
from random import choice

RULES = 'What is the result of the expression?'


def pass_game():
    rand_num1 = randint(1, 100)
    rand_num2 = randint(1, 100)
    rand_symbol = choice(['+', '-', '*'])
    ques = str(rand_num1) + ' ' + str(rand_symbol) + ' ' + str(rand_num2)
    if rand_symbol == '+':
        right_answer = str(rand_num1 + rand_num2)
    elif rand_symbol == '-':
        right_answer = str(rand_num1 - rand_num2)
    elif rand_symbol == '*':
        right_answer = str(rand_num1 * rand_num2)
    return ques, right_answer

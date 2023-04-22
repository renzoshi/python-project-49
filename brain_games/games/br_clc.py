from random import randint
from random import choice

RULES = 'What is the result of the expression?'
START_LIMIT = 1
FINISH_LIMIT = 100
OPERATOR = ('+', '-', '*')


def get_start_game():
    rand_num1 = randint(START_LIMIT, FINISH_LIMIT)
    rand_num2 = randint(START_LIMIT, FINISH_LIMIT)
    rand_symbol = choice(OPERATOR)
    question = str(rand_num1) + ' ' + str(rand_symbol) + ' ' + str(rand_num2)
    right_answer = str(calculated(rand_num1, rand_num2, rand_symbol))
    return question, right_answer


def calculated(rand_num1, rand_num2, rand_symbol):
    if rand_symbol == '+':
        result = str(rand_num1 + rand_num2)
    elif rand_symbol == '-':
        result = str(rand_num1 - rand_num2)
    elif rand_symbol == '*':
        result = str(rand_num1 * rand_num2)
    return result

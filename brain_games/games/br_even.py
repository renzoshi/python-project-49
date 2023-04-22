from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
START_LIMIT = 1
FINISH_LIMIT = 100


def is_even(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_start_game():
    rand_num = randint(START_LIMIT, FINISH_LIMIT)
    question = rand_num
    right_answer = str(is_even(question))
    return question, right_answer

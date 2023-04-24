from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
START_LIMIT = 1
FINISH_LIMIT = 100


def is_even(question):
    if question % 2 == 0:
        return True
    else:
        return False


def get_start_game():
    rand_num = randint(START_LIMIT, FINISH_LIMIT)
    question = rand_num
    if is_even(question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer

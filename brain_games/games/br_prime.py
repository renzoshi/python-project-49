from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_LIMIT = 1
FINISH_LIMIT = 100


def is_prime(rand_num):
    if rand_num < 2:
        return 'no'
    for i in range(2, int(rand_num ** 0.5 + START_LIMIT)):
        if rand_num % i == 0:
            return 'no'
    else:
        return 'yes'


def get_start_game():
    rand_num = randint(START_LIMIT, FINISH_LIMIT)
    question = rand_num
    right_answer = str(is_prime(question))
    return question, right_answer

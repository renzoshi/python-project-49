from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_LIMIT = 1
FINISH_LIMIT = 100


def is_prime(rand_num):
    if rand_num < 2:
        return False
    for i in range(2, int(rand_num ** 0.5 + START_LIMIT)):
        if rand_num % i == 0:
            return False
    else:
        return True


def get_start_game():
    rand_num = randint(START_LIMIT, FINISH_LIMIT)
    question = rand_num
    if is_prime(rand_num):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer

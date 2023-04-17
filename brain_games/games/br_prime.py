from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_logic(rand_num):
    if rand_num < 2:
        return False
    for i in range(2, int(rand_num ** 0.5 + 1)):
        if rand_num % i == 0:
            return False
    else:
        return True


def pass_game():
    rand_num = randint(1, 100)
    ques = rand_num
    if prime_logic(rand_num):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return ques, right_answer

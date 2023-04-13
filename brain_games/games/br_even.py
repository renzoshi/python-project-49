from random import randint 

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(rand_num):
    return rand_num % 2 == 0

def pass_game():
    rand_num = randint(1, 100)

    if is_even(rand_num):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    ques = rand_num
    return ques, right_answer

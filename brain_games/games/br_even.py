from random import randint 

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

def pass_game():
    rand_num = randint(1, 100)

    if rand_num % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    ques = rand_num
    return ques, right_answer

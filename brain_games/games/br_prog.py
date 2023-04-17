from random import randint


RULES = 'What number is missing in the progression?'

def pass_game():
    
    games_list = []
    rand_start = randint(1,20)
    rand_length = randint(5, 13)
    rand_step = randint(1, 13)
    for i in range(rand_length):
        rand_start += rand_step
        games_list.append(rand_start)
    prog_index = randint(1, rand_length - 1)
    right_answer = str(games_list[prog_index])
    games_list[prog_index] = '..'
    ques = ' '.join(map(str, games_list))
    return ques, right_answer
    
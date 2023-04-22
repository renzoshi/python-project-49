from random import randint


RULES = 'What number is missing in the progression?'
MIN_LIMIT = 1 
START_LIMIT = 20 
STEP_LIMIT = 13
START_LENGHT = 5
FINISH_LENGHT = 13


def progression(rand_start, rand_length, rand_step):
    game_list = []
    for i in range(rand_length):
        rand_start += rand_step
        game_list.append(rand_start)
    return game_list


def get_start_game():
    rand_start = randint(MIN_LIMIT, START_LIMIT)
    rand_length = randint(START_LENGHT, FINISH_LENGHT)
    rand_step = randint(MIN_LIMIT, STEP_LIMIT)
    rand_progression = progression(rand_start, rand_length, rand_step)
    prog_index = randint(MIN_LIMIT, len(rand_progression) - 1)
    right_answer = str(rand_progression[prog_index])
    rand_progression[prog_index] = '..'
    question = ' '.join(map(str, rand_progression))
    return question, right_answer

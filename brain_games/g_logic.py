import prompt


ROUND = 3


def launch_game(games):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print('Hello, ' + name + '!')
    print(open.RULES)
    for _ in range(ROUND):
        question, right_answer = games.get_start_game()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer.lower() != right_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'."
                  f"\nLet's try again, {name}!")
            return
    print('Correct!')

    print('Congratulations, ' + name + '!')

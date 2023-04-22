import prompt


ROUND = 3


def launch_game(open):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print('Hello, ' + name + '!')
    print(open.RULES)
    for _ in range(ROUND):
        question, right_answer = open.get_start_game()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer == right_answer or answer == right_answer.capitalize():
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'."
                  f"\nLet's try again, {name}!")
            return

    print('Congratulations, ' + name + '!')

import prompt


def welcome_user():
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print('Hello, ' + name + '!')


def opening(open):
    welcome_user()
    print(open.RULES)
    i = 0

    while i < 3:
        ques, right_answer = open.pass_game()
        print('Question: ' + str(ques))
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{right_answer}'.")
            print("Let's try again, " + name + '!')
            return
        i = i + 1

    print('Congratulations, ' + name + '!')

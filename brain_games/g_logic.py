import prompt 
ROUND = 3 


def opening (open):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print('Hello, ' + name +'!')
    print(open.RULES)
    i = 0 

    while i < ROUND:
        ques, right_answer = open.pass_game()
        print('Question: ' + str(ques))
        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print("Let's try again, " + name + '!')

            return
        i = i + 1

    print('Congratulations, ' + name + '!')
import prompt

def opening():
    print('Welcome to the Brain Games!')

def welcome_user():
    global name
    name = prompt.string('What is you name? ')
    print('Hello, ' + name + '!')

def ending():
    print('Congratulations ' + name + '!')

def question1():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: 15')
    answer = prompt.string('You answer: ')
    if answer == 'no':
        print('Correct!')
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'")
        print("Let's try again, " + name + "!")
        quit()

def question2():
    print('Question: 6')
    answer = prompt.string('You answer: ')
    if answer == 'yes':
        print('Correct!')
    else:
        print("'no' is wrong answer ;(. Correct answer was 'yes'")
        print("Let's try again, " + name + "!")
        quit()


def question3():
    print('Question: 7')
    answer = prompt.string('You answer: ')
    if answer == 'no':
        print('Correct!')
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'")
        print("Let's try again," +  name + "!")        
        quit() 

def main():
    opening()
    welcome_user()
    question1()
    question2()
    question3()
    ending()
    
 

if __name__ == '__main__':
    main()
    

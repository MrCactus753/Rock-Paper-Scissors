from random import choice


# functions
def options(opt ='rock,scissors,paper'):
    if len(opt)>0:
        ls = opt.split(',')
    else:
        ls = ['rock', 'paper', 'scissors']
    different_combinations = {i:(ls[ls.index(i)::] + ls[:ls.index(i)])[:int(((len(ls)-1)/2)):-1] for i in ls}
    return ls, different_combinations


def win_checker(x, choi, opt):
    global score
    combinations = opt[1]
    computer_pick = choi
    user_pick = x
    if user_pick == computer_pick:
        print('There is a draw (%s)' % computer_pick)
        score += 50
    elif computer_pick in combinations[user_pick]:
        print('Well done. Computer chose %s and failed' % computer_pick)
        score += 100
    else:
        print('Sorry, but the computer chose %s' % computer_pick)



def mainloop():
    global score
    oprionsresult = options(input())
    print("Okay, let's start")
    #print(oprionsresult[1])
    while True:
        a = input()
        computer_choice = choice(oprionsresult[0])#input('>')
        if a == '!exit':
            print('Bye!')
            break
        elif a == '!rating':
            print('Your rating: %s' % str(score))
        elif a in oprionsresult[1].keys():
            win_checker(a, computer_choice, oprionsresult)
        else:
            print('Invalid input')
            pass


def file_handler():
    name = input('Enter your name: ')
    print('Hello, %s' % name)
    with open('rating.txt', 'r') as f:
        users = [i.split() for i in [i.rstrip('\n') for i in f.readlines()]]
        for s in users:
            if s[0] == name:
                return int(s[1])
            else:
                return 0


# main loop
score = file_handler()
mainloop()



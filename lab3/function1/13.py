import random

def guess_the_num():
    r = random.randint(1,20)
    print("Hello! What is your name?")
    name = input()
    print("Well,", name + ',',"I am thinking of a number between 1 and 20." )
    print('Take a guess.')
    num = int(input())
    guesses = 1
    while(num != r):
        if num < r:
            print('Your guess is too low.')
            print('Take a guess.')
        else:
            print('Your guess is too high')
            print('Take a guess.')
        num = int(input())
        guesses += 1
    else:
        print('Good job,',name + '!','You guessed my number in', guesses,'guesses!')
        
guess_the_num()
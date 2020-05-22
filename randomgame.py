from random import randint
import sys
# generate a number 1~10
a = int(sys.argv[1]) 
b = int(sys.argv[2])
answer = randint(a,b)
# you can only give it try for 5 times
print(' how many tryes does the player gets : ')
c = int(input())
chances = 0

#input from user?
#check that input is a number 1~10
while chances < c:
    try:
        guess = int(input('guess a number between {} ~ {}: '.format(a,b)))
        if  a < guess < b:
            if int(guess) == answer:
                print(' you are a genius!!!!!')
                break
            elif guess < answer:
                print('Your guess is lower : Guess a number higher than',guess)
                chances += 1 
            else:
                print('Your guess is higher: Guess a number lower than',guess)
                chances += 1 
        else:
            print('hey DUMBOOOOOO!!!!! i said {} to {} '.format(a,b))
            print('you have entered',guess)
            chances += 1 
    except ValueError:
        print(' please enter a number')
        continue
         

if not chances < c:
    print("You LOST!!!!! the answer is: ",answer)
    
# ask again

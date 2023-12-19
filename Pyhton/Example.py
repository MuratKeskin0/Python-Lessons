import random
number=random.randint(1,100)
attempt=5
count = 0
correct_guess = False

while attempt >0:
    attempt-=1
    count+=1
    guess= int(input('Guess: '))

    if(number == guess):
       print(f'Great job! Attempt: {count}, your total point: {100-(20)*(count-1)}')
       correct_guess=True
       break
    elif (number > guess):
        print('up')
    else:
        print('down')

if not correct_guess:
    print(f'you exceed your attempts number. The number was: {number}, your point is zero')
import random 

choice = int(input('Pick the first number you want your guess in between: '))
choice_2 = int(input('Pick the second number you want you guess in between: '))
secret = random.randint(choice, choice_2)

while True:
    guess = int(input('Take a Guess: '))
    if guess == secret:
        print ('You Win!')
        break
    elif guess < secret:
        print ('Too Low')
    else:
        print ('Too High')
# a simple guessing game
# written by Murray Coueslant 2017/09/22

animal = 'Lion'

while 1:
    print('I am thinking of an animal.')
    guess = input('What do you think it is?: ')
    if guess == animal:
        print('Well done! You guessed right.')
        quit()
    elif guess.lower() == 'quit':
        print('Thanks for playing!')
        quit()
    else:
        print("Sorry, that isn't right, try again!")

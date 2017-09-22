# a simple guessing game
# written by Murray Coueslant 2017/09/22

animal = 'lion'


def askUser(animal):
    pref = input('Do you like ' + animal + 's?(Y or N):')
    if pref.lower() == 'y':
        print("I'm glad you like", animal + 's.')
        quit()
    else:
        print("That's a shame,", animal + 's', 'are great creatures.')


while 1:
    print('I am thinking of an animal.')
    guess = input('What do you think it is?: ')
    if guess[0].lower() == 'q':
        print('Thanks for playing!')
        quit()
    elif guess.lower() == animal.lower():
        print('Well done! You guessed right.')
        askUser(animal)
        quit()
    else:
        print("Sorry, that isn't right, try again!")

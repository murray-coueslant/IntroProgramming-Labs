import random      # emotion  reward      punish     threaten joke
personalityTable = [["anger", "surprise", "sadness", "anger", "anger"],
                    ["disgust", "anger", "anger", "anger", "anger"],
                    ["fear", "disgust", "disgust", "sadness", "disgust"],
                    ["happiness", "happiness", "sadness", "fear", "happiness"],
                    ["sadness", "happiness", "fear", "anger", "happiness"],
                    ["surprise", "happiness", "anger", "disgust", "happiness"]]

# get the interaction from the user and return an integer corresponding to the column in the table above
#     params: none
#     input: user interaction
#     returns: corresponding integer
def getInteraction():
    interaction = input('Enter the interaction you would like to have with the personality: ').lower()
    if interaction == 'reward':
        return 1
    elif interaction == 'punish':
        return 2
    elif interaction == 'threaten':
        return 3
    elif interaction == 'joke':
        return 4
    else:
        return 0


# search the table for the current emotion and return the emotion following the user interaction
#     params: current emotion, user interaction
#     input: none
#     returns: new emotion
def lookupEmotion(currentEmotion, userInteraction):
    for row in personalityTable:
        if row[0] == currentEmotion:
            return row[userInteraction]


# display the current emotion of the personality using print
#     params: current emotion
#     input: none
#     returns: none
#     output: message corresponding to current emotion
def displayEmotion(currentEmotion):
    if currentEmotion == 'anger':
        print('You\'re making me very angry!')
    elif currentEmotion == 'disgust':
        print('You\'re a horrid person!')
    elif currentEmotion == 'fear':
        print('You\'re scaring me!')
    elif currentEmotion == 'happiness':
        print('I\'ve got a big smile on my face!')
    elif currentEmotion == 'sadness':
        print('You should wipe the tears from my eyes.')
    else:
        print('What a surprise!')


print("Welcome to the personality, enjoy interacting with it through four commands. Threaten, punish, joke or reward.")
newEmotion = personalityTable[random.randint(0, 5)][0]
currentEmotion = newEmotion
while 1:
    displayEmotion(currentEmotion)
    userInteraction = getInteraction()
    while userInteraction == 0:
        print("Incorrect interaction, enter another.")
        userInteraction = getInteraction()
    newEmotion = lookupEmotion(currentEmotion, userInteraction)
    currentEmotion = newEmotion

import random
from graphics import *
                   # emotion  reward      punish     threaten joke
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
def getInteraction(app, inputBox):
    while app.getKey() != "Return": pass
    interaction = inputBox.getText()
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
        return 'You\'re making me very angry!'
    elif currentEmotion == 'disgust':
        return 'You\'re a horrid person!'
    elif currentEmotion == 'fear':
        return 'You\'re scaring me!'
    elif currentEmotion == 'happiness':
        return 'I\'ve got a big smile on my face!'
    elif currentEmotion == 'sadness':
        return 'You should wipe the tears from my eyes.'
    else:
        return 'What a surprise!'


newEmotion = personalityTable[random.randint(0, 5)][0]
currentEmotion = newEmotion
app = GraphWin("Personality", 400, 200)
app.setCoords(0, 0, 10, 10)

Text(Point(5,9), "Welcome to the personality, interact with it through four commands.").draw(app)
Text(Point(5,8), "Threaten, punish, joke or reward.").draw(app)
output1 = Text(Point(4,7), "I am currently feeling " + currentEmotion).draw(app)
output2 = Text(Point(4,5), displayEmotion(currentEmotion)).draw(app)
Text(Point(4,3), "What would you like to do?: ").draw(app)

inputBox = Entry(Point(8,3), 10)
inputBox.draw(app)
while 1:
    output1.setText("I am currently feeling " + currentEmotion)
    output2.setText(displayEmotion(currentEmotion))
    userInteraction = getInteraction(app, inputBox)
    while userInteraction == 0:
        print("Incorrect interaction, enter another.")
        userInteraction = getInteraction()
    newEmotion = lookupEmotion(currentEmotion, userInteraction)
    currentEmotion = newEmotion

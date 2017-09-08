# A program for the user to create their own mad libs sentence
# Written by: Murray Coueslant, Date: 2017-09-08
# Flag variable which is used to ask the user if they want to make more sentences
flag = 'Y'

# main while loop
while flag == 'Y':
    flag == 'N'

    # User input section, takes the four inputs required for the sentence
    verb = input('Enter a verb: ')
    noun = input('Enter a noun: ')
    adje = input('Enter an adjective: ')
    place = input('Enter a place: ')

    # output statement for the sentence
    print("Bring your", adje, noun, "and", verb, "it at the", place)

    # asking the user if they want to create another sentence
    flag = input("Make another? (Y or N): ")


# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Murray Coueslant
# Created: 2017-09-28


def main():
    uname = userCreate()
    passwd = passCreate()
    print("Account configured. Your new email address is", uname + "@marist.edu")


def getNames():
    # get user's first and last names
    first = input("Enter your first name: ").lower()
    last = input("Enter your last name: ").lower()
    nameList = [first, last]
    return nameList


def userCreate():
    names = getNames()
    # create marist style username
    uname = names[0] + '.' + names[1]
    return uname


def passCreate():
    # ask user to create a new password
    passwd = input("Create a new password: ")
    strength = checkStrength(passwd)
    # do not allow the user to create a password shorter than 8 chars
    while strength is False:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
        strength = checkStrength(passwd)
    print("The force is strong in this one…")
    return passwd


def checkStrength(password):
    lowerPass = password.lower()
    upperPass = password.upper()
    if len(password) < 8 or lowerPass == password or upperPass == password:
        return False
    else:
        return True


main()
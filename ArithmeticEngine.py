# CMPT 120 - Lab #6
# Murray Coueslant
# 26-OCT-2017
###


def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")


def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")


def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower()
        if cmd == "add":
            num1, num2 = getNums()
            result = num1 + num2
            printResult(result)
        elif cmd == "sub":
            num1, num2 = getNums()
            result = num1 - num2
            printResult(result)
        elif cmd == "mult":
            num1, num2 = getNums()
            result = num1 * num2
            printResult(result)
        elif cmd == "div":
            num1, num2 = getNums()
            result = num1 // num2
            printResult(result)
        elif cmd == "quit":
            break
        else:
            print("\'" + cmd + "\' is not a command.")

def printResult(result):
    print("The result is " + str(result) + ".\n")


def getNums():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1, num2


def main():
    showIntro()
    doLoop()
    showOutro()


main()

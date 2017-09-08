# Introduction to Programming
# Author: Murray Coueslant
# Date: 2017/09/01


def main():
    print('Hello, instructor!')
    print('Good-bye!')
main()


def greet(name):
    instructor_name = name
    print('Hello', instructor_name + '!')
    print('Good-bye', instructor_name + '!')
greet(input('Enter the name of the person you want to greet: '))

# A program which approximates the value of pi by summing the terms of a series up to the nth term defined by the user
# Written by Murray Coueslant, Date: 2017/09/15

import math

def approxPi(n):
    numerator = 4
    denominator = 1
    sum = 0
    for i in range(1, n):
        if i % 2 == 1:
            sum += (numerator / denominator)
        elif i % 2 == 0:
            sum -= (numerator / denominator)
        denominator += 2
    difference = math.pi - sum
    print('The value we have approximated for pi is:', sum)
    print('The difference between it and the actual value of pi is:', difference)


while 1:
    approxPi(int(input('Enter a term to sum the series up to: ')))
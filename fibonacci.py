# A program to calculate the fibonacci numbers up to a certain term
# Written by: Murray Coueslant, Date: 2017/09/15


def fib(n):
    fib1 = 0
    fib2 = 1
    result = 0
    if n == 1 or n == 2:
        result = fib2
    else:
        for i in range(0, n-1):
            result = fib1 + fib2
            fib1 = fib2
            fib2 = result
    print(result)


while 1:
    fib(int(input('Enter a term to calculate the sequence upto: ')))

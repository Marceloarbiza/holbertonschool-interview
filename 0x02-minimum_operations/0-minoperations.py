#!/usr/bin/python3
""" min operations """


def minOperations(n):
    """min operations func """
    minOP = 0
    div = 2
    while isinstance(n, int) and n > 1:
        while n % div:
            div += 1
        minOP += div
        n = int(n / div)
    return minOP

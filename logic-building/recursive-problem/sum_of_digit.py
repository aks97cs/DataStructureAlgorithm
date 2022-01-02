""" Program to get sum of digit
"""

def recur(num):
    sum = 0
    if num <= 1:
        return num
    return (num%10) + recur(int(num/10))
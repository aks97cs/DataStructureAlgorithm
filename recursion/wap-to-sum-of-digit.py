"""
program to recusively give some of digit
"""

def sumOfDigit(num):

    if num%10 == num:
        return num
    
    rem = num % 10
    num = num - rem
    num = num/10

    return rem + sumOfDigit(num)


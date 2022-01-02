""" Program to get nth fabnocci series
"""


def recur(num, a=0, b=1, k=1):

    if k == num or k > num:
        return 
    if k == 1:
        print(a, end=" ")
        print(b, end=" ")
        return recur(num, a, a+b, k+1)
    print(a+b, end=" ")
    return recur(num, b, a+b, k+1)

if __name__ == '__main__':
    recur(4)

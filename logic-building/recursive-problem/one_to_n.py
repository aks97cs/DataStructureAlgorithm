""" Program to print one to N
"""

def recur(num):
    if num == 1:
        print(num)
        return
    recur(num-1)
    print(num)
    return

if __name__ == '__main__':
    recur(10)
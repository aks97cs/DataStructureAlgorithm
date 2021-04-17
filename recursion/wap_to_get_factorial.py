"""
@desc: programm to find the factorial value recursively
"""

def fact(num):

    if num == 0:
        return 1
    return num*fact(num-1)


if __name__ == "__main__":

    num = int(input("Enter the value : "))

    print(fact(num))
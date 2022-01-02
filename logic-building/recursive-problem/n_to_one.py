""" Program to print N to one using recusion
"""

def recur(num:int):
    if num == 1:
        print(num)
        return
    print(num)
    return recur(num-1)
if __name__ == "__main__":
    recur(10)
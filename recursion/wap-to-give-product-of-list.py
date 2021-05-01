"""
recusive program to print product of list 
input = list of numbers
"""

def productOfList(arr, leng):
    if leng == 0:
        return arr[leng]
    return arr[leng] * productOfList(arr, leng-1)

    pass

if __name__ == '__main__':
    arr = [int(num) for num in input("Enter the multiple value\n").split(", ")]

    print(productOfList(arr, len(arr)-1))

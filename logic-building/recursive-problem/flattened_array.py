"""
Write a recursive function that takes an array that may contain more arrays in it and returns an array with all values flattened.
"""


def flatten(arr):
    res = []
    for i in arr:
        if type(i) is list:
            res.extend(flatten(i))
        else:
            res.append(i)
    return res

"""
[1, 2]
1:  start time
2: end time
I/P: [[2,3], [1,4], [5, 8], [6, 10]]
O/P: 2
"""

def optimiser(arr):
    count = 0
    index = 0
    for i in range(1, len(arr)):
        if i == 1:
            count += 1
        if arr[index][1] < arr[i][0]  and arr[index][1] < arr[i][1]:
            count += 1
            index = i
    return count

"""
1.Takes input an array of numbers. The numbers in the input array can be negative, positive,
decimal and in any order.
2. Re arrange numbers in the array as follows
a1 <= a2  >= a3 <= a4 >= ...
3. Returns the array with re-arranged numbers as defined in Step 2.

Testcase: 
arr  = [1,2,3,4,5,6,7,8]
arr = []
arr = [-1, -3]
arr = [-1, -3, 2, 0]
arr = [1,2,0,4,5,6,7,8]

Time complexity: O(n)
Space complexity: O(1)
"""

def func(arr) -> list:
    if len(arr):
        for i in range(1, len(arr)):
            if i % 2 == 0:
                if arr[i-1] < arr[i]:
                    arr[i-1], arr[i] = arr[i], arr[i-1]
            elif arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr


if __name__ == "__main__":
    arr  = [1,2,3,4,5,6,7,8]
    print(func(arr))

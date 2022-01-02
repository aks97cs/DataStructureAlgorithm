"""
return index
time complexity: O(log n)
"""

def func(arr, num) -> int:
    low, high = 0, len(arr)-1
    mid = (low+high)/2
    while low<=high:
        mid = int((low+high)/2)
        if arr[mid] == num:
            return f"element found at index {mid}"
        if num < arr[mid]:
            high = mid -1
        else:
            low = mid + 1
    return "Not Found"



# recursive solution
def recur(arr, num, low, high) -> int:
    if not(low<=high):
        return -1
    mid = int((low+high)/2)
    print(mid, high, low)
    if arr[mid] == num:
        return mid
    if num < arr[mid]:
        return recur(arr, num, low, mid-1)
    else:
        return recur(arr, num, mid+1, high)

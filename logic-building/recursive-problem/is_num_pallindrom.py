"""
"""

def is_num_palindrom(num, rev=0):
    if num == 0:
        return rev
    r = num%10
    num = num - r
    num = int(num/10)
    return is_num_palindrom(num, rev*10+r)

num = 1221
if is_num_palindrom(num) == num:
    print(True)
else:
    print(False)
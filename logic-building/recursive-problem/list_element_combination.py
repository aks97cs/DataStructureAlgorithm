"""
I/P: [1,2,3]
O?P: [[1], [1,2], [1,2,3], [2], [2,3], [3])
"""

from itertools import chain, combinations

ss = [1,2,3]

def all_subsets(ss):
    return list(chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1))))

all_subsets(ss)


# for subset in all_subsets(ss):
#     print(subset)

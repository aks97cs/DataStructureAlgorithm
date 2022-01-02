# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


def func(head):

    bucket = set()
    temp = head
    while (temp):
        
        if (temp in bucket):
            break
        bucket.add(temp)
        temp = temp.next
    print("bucket ==", bucket)
    return len(bucket)


def reverseInGroups(arr, N=5, K=3):
    # code here
    # ret = []
    for i in range(0, N+K, K):
        print("for i =", i, K+i)
        if len(arr[i:]) < K:
            arr[i:] = arr[i:][::-1]
            break
        print(arr[i:i+K])
        arr[i:i+K] = (arr[i:i+K][::-1])
    return arr

if __name__ == "__main__":
    arr = ['36', '93', '64', '48', '96', '55', '70', '0', '82', '30', '16', '22', '38', '53', '19', '50', '91', '43', '70', '88', '10', '57', '14', '94', '13', '36', '59', '32', '54', '58', '18', '82', '67']
    print(reverseInGroups(arr, 33, 13))

    # h1 = Node(1)
    # node2 = Node(2)
    # h1.next = node2

    # node = Node(3)
    # h1.next.next = node
    # node = Node(4)
    # h1.next.next.next = node

    # node = Node(5)
    # h1.next.next.next.next = node

    # node = Node(4)
    # h1.next.next.next.next.next = node2
    # arr = func(h1)
    # print(arr)
    # arr = h1

    # while True:

    #     if arr is None:
    #         break
    #     print(arr.data)
    #     arr = arr.next

# get_series(arr)



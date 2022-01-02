#User function Template for python3
"""
start = 2 4 4 8 7
end = 10 7 8 8 10
output = 2
"""
class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n=5,start=[2,1,4,9,1], end= [9,5,4,10,3]):
        count = 1
        index = 0
        for i in range(0, n):
            for j in range(i+1, n):
                if end[j] < end[i]:
                    start[i], start[j]= start[j], start[i]
                    end[i], end[j] = end[j], end[i]
        for i in range(1, n):
            if end[index] < start[i]:
                index = i
                count +=1
        return count

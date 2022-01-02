"""
desc : Write a recursive function that takes a number and returns the sum of all the numbers from zero to that number.
"""

def cumulative_sum(num):
	
	if num == 1:
		return num
	return num+cumulative_sum(num-1)

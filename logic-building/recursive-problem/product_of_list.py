"""
Write a recursive function that takes a list of numbers as an input and returns the product of all the numbers in the list.
"""

def product(arr):
	
	if len(arr) == 1:
		return arr[0]
	return arr[len(arr)-1] * product(arr[:-1])

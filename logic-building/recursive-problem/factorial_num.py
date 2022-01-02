"""
Write a recursive function that takes a number as an input and returns the factorial of that number.
"""

def factorial_num(num):
	
	if num == 1:
		return num
	return num * factorial_num(num-1)

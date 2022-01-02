"""
Write a function that takes a string and returns if the string is a palindrome.
"""

def is_palindrome(str):
	
	if len(str)==0:
		return True
	if str[:1] != str[-1]:
		return False
	return is_palindrome(str[1:-1])

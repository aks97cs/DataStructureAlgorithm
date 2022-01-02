"""
Write a function that takes a string and returns reverse of string.
"""

def palindrom_string(str):
	
	if len(str) == 1:
		return str
	return palindrom_string(str[1:]) + str[:1]

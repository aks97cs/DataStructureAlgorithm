""" Given a string, print all possible palindromic partitions
"""

def recurr(strg):
	ret = []
	if len(strg) == 0 or len(strg) < 1:
		return ''
	if str[:-1:-1] == recurr(strg[:-1]):
		ret.append(strg[:-1])
	return  ret

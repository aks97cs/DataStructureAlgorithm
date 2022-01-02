"""
String subset cobination
"""

def subset_combination(strg):
	s= []
	s1 = []
	if len(strg) == 0 or len(strg) < 1:
		return []
	s1 = s1+ [strg] + subset_combination(strg[:-1])
	s = s + subset_combination(strg[1:])
	return  list(set().union(s1,s))


""" rope cutting
"""

def recur(n, a, b, c):

	if n ==0:
		return 0
	if n < 0:
		return -1

	res = max(
		recur(n-a, a, b, c),
		recur(n-b, a, b, c),
		recur(n-c, a, b, c)
		)

	if res == -1:
		return -1
	return res + 1
	
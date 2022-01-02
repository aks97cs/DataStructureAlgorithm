"""
Write a recursive function that will return the sum of all the positive numbers in a dictionary which may contain more dictionaries nested in it.
"""

def dict_sum(data):
	sum_num = 0
	for key in data.keys():
		if type(data[key]) == dict:
			sum_num = sum_num + dict_sum(data[key])
		elif type(data[key]) == int:
			sum_num = sum_num + data[key]
	return sum_num

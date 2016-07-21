#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
#
# Your code should run in Theta(n) time
#

def minimize_absolute(L):
	# your code here
	return sorted(L)[len(L)/2]
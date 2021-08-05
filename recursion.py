#!/opt/miniconda/bin/python

'''fibonacci(n) - returns the nth term in the fibonacci series'''
def fibonacci(n):
	if n < 0:
		return 'incorrect input'
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

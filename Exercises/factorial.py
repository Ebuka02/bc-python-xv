import functools

from funtools import reduce

def recur(n):
	reduce(lambda x,y: x+y, range(1,n+1))



def fact(n):
	if n==0 and n==1:
		return 1
	else:
		return n*fact(n-1)

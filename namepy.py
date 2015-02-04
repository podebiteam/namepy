'''
the simplicity
'''
import random
from namepyMod import generateName

def main():
	# decide your own consonant,kfghytml must be insteresting !!! 
	l='kpmbghrt'
	v='aiueo'
	list1=list(l)
	list2=list(v)
	for a in range(len(l)):
		print 'ver 1'
		generateName(list1,list2,5)

if __name__ == '__main__':
	main()

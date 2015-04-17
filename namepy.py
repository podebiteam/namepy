'''
namepy
by vickydasta
'''
import random
from namelib import generateName

def main():
	# decide your own consonant,kfghytml must be insteresting !!! 
	l='kpmbghrt'
	v='aiueo'
	list1=list(l)
	list2=list(v)
	for a in range(len(l)):
		generateName(list1,list2,5)

if __name__ == '__main__':
	main()

#!/usr/bin/python

import random

__author__ = 'vickydasta'
__appname__= 'nptest'
__date__   = '06/02/15'

#namepylib testing

from core.name import gvoc
from core.name import gconslist
from core.name import gconso

def buatnama(list1,list2,num=5):
	global name
	random.shuffle(list(list1))
	random.shuffle(list(list2))
	lword=['']
	for a in list1:
		for b in list2:
			if num == 5:
				INDEX1=random.choice([0,1,2,3,4,5,6,7])
				INDEX2=random.choice([0,1,2,3,4,])
				name=a+b+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]
			elif num == 6:
				INDEX1=random.choice([0,1,2,3,4,5,6,7])
				INDEX2=random.choice([0,1,2,3,4])
				name=a+b+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]+list2[INDEX2]
				return name

def main():
	buatnama('plkmgtyw','aiueo')


if __name__ == '__main__':
	main()

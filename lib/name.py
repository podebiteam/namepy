#!/usr/bin/env python
PYTHONDEBUG=1
import random
import urllib2
import string
import requests
from random import shuffle as randomize

u='http://'
lang='' #set default lang as empty string
remote_host = 'wiktionary.org/wiki'
remote_host_ = 'www.wordnik.com'
url=u+lang+remote_host

def findwordmeaning(word):
    req = requests.get('https://en.wiktionary.org/wiki/'+word)
    if 'Wiktionary does not yet have an entry for '+word not in req:
        return False
    else:
    	return True

def getalph():
	return string.letters

def vocal():
	return 'aiueo'

def name_meaning_present(name):
	pass #bugy,remove pass to know,if name meaning is present
	global status
	status = ''
	url=urllib2.urlopen('http://www.morewords.com/word/'+name)
	read_data=url.read()
	if re.findall("No words found in this wordlist when searching for",read_data) != []:
		return True
	else:
		return False

def generate_5(list1,list2,num=5):
	# set default name length into 5
	# if num != 5
	# return name with length 6
	# PS : num length defaultly is 5 or 6
	global final
	final = ''
	#randomize list
	new_list=randomize(list1)
	for a in new_list:
		if num == 5:
			INDEX1=random.choice([0,1,2,3,4,5,6,7])
			INDEX2=random.choice([0,1,2,3,4,])
			return list2[INDEX2]+list1[INDEX1]+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]
		elif num == 6:
			INDEX1=random.choice([0,1,2,3,4,5,6,7])
			INDEX2=random.choice([0,1,2,3,4])
			return list2[INDEX2]+a+list2[INDEX2]+list1[INDEX2]+list2[INDEX2]+list1[INDEX2]


def generateName(list__,list_,num=5):
	global final
	name = ''
	#randomize list
	for a in list1:
		for b in list2:
			if num == 5:
				rang_name=random.choice([0,1,2,3,4,5,6,7])
				rang_name_=random.choice([0,1,2,3,4,])
				return a+b+list__[rang_name_]+list_[rang_name_]+list__[rang_name_]
			elif num == 6:
				rang_name=random.choice([0,1,2,3,4,5,6,7])
				rang_name_=random.choice([0,1,2,3,4])
				return a+b+list1[rang_name_]+list2[rang_name_]+list1[rang_name]+list2[rang_name_]

def DetectRegion(name,knwon=False):
	'''
	region detector,currently on development
	'''
	global region
	region = ''
	'''
	example :
	if name = 'sarkov'
	so it must be Russian name,because of there's "v" on the end of the name
	or name = 'suryo'
	it must be Javanese name,signed by "s" on the first and "o" on the last
	'''
	if name:
		if len(name) == 5:
			#start analyzing name
			if name[4] in 'zjv':
				region= 'Russian'
			elif name[0] == 's' and name[4] == '0':
				region='Java Island (Indonesia)'
			elif name[4] == 'y' and name[0] != 'v' and name[1] != 'i' and name[2] != 'c':
				region = 'Chile ('
			return

def G5(list1,list2):
	#select random alphabet
	for char in list1:
		for b in list2:
			i=random.choice([0,1,2,3,4,5,6,7])
			ind=random.choice([0,1,2,3,4,])
			return a+b+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]


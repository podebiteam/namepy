#!/usr/bin/env python

__author__  = 'vickydasta'
__date__    = '05/02/2015'
__apps__    = 'namepy module'
__version__ = '1.2'

import random,urllib2
from random import shuffle as randomize

cons=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
      'p', 'q',  'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
voc=['a','i','u','e','e']
hy=random.choice([0,1,2,3,4,5,6,7])
hx=random.choice([0,1,2,3,4,])

#present_word = ['acuh','amin','antah','']

def checkdb(sa,s):
    with open(txt,'r') as re:
        text=re.readlines()
        if text == s:
            stat = 'present '
        else:
            stat = 'not'
        return stat


def gvoc():
    'return vocal alph'
    return 'aiueo'
    #make it simpler dude

def gconslist():
    return ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n','p', 'q',  'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def gconso(conslist):
    'return random consonant'
    c=conslist
    hy=[0,1,2,3,4,5,6,7]
    randomize(hy)
    randomize(conslist)
    r=random.choice(hy)
    s=random.choice(hy)
    t=random.choice(hy)
    u=random.choice(hy)
    v=random.choice(hy)
    w=random.choice(hy)
    x=random.choice(hy)
    y=random.choice(hy)
    randconst=c[r]+c[s]+c[t]+c[u]+c[v]+c[w]+c[x]+c[u]
    return randconst

'''def name_meaning_present(lang='ind',name):

	many parents confused to decide
    which name is used to his son/daughter's name
	and much affraid of these name
    is was used by another kids
    (in this case the parent who won't to be mainstream)
	this situation
    pretty much simple in my head.
	another one situation is taking
    name to something like mountaint maybe,
    or for some unnamed storm out there ?
	name_meaning_present(name) --> checking whether the name has a mean or not
	generateName(list1, list2, num=5) --> generate random name from list with len(num)
	region_detector --> detect name region based on it signature
    (because i believe in fact that every name has it's own signature)
	pass #bugy,remove pass to know,if name mean is present
	global status
	status = ''
	url=urllib2.urlopen('http://www.morewords.com/word/'+name)
	read_data=url.read()
	if re.findall("No words found in this wordlist when searching for",read_data) != []:
		status = 'Present'
	else:
		status='Unpresent'
	return status

'''

'''
def generateNames(list1,list2,num=5):
    if len(list1) != 8 and len(list2) !=5:
        pass
    else:
        global final
        final = '';
        l=list(list1)
        randomize(l)
        for a in l:
           	for b in list1:
                   l=random.choice([0,1,2,3,4,5,6,7])
                   j=random.choice([0,1,2,3,4,])
                   final=list2[j]+list1[l]+list1[j]+list2[l]+list1[j]
                   if checkdb('db.txt',final) == 'not':
                       print final
                   else:
                       pass'''

def generateName(list1,list2,num=5):
	global final
	final = ''
	#randomize list
	for a in list1:
		for b in list2:
			if num == 5:
				INDEX1=random.choice([0,1,2,3,4,5,6,7])
				INDEX2=random.choice([0,1,2,3,4,])
				final=a+b+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]
			elif num == 6:
				INDEX1=random.choice([0,1,2,3,4,5,6,7])
				INDEX2=random.choice([0,1,2,3,4])
				final=a+b+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]+list2[INDEX2]
			return final

def region_detector(name):
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
				region = 'Chile'
			return region
		else:
			pass
	else:
		pass


def gencheck(list1,list2):
	pass
	'''generate random name with random alphabet
	'''
	#select random alphabet
	pass
	for a in list1:
		for b in list2:
			INDEX1=random.choice([0,1,2,3,4,5,6,7])
			INDEX2=random.choice([0,1,2,3,4,])
			final=a+b+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]
			global detect_region
			detect_region = region_detector(final)
			if detect_region == '':
				res = 'unmatch with current database'
			else:
				pass

			if final != None:
				res = 'match found'
				print 'Current Name : {}'.format(final)
				print 'status : '+ res
				print '{} comes from --> '.format(final),region_detector(final)
			else:
				pass

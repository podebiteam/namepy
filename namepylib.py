#!/usr/bin/env python

__author__  = 'vickydasta'
__date__    = '05/02/2015'
__apps__    = 'namepylib'
__version__ = '1.3'

import random,urllib2
from random import shuffle as randomize

cons=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
      'p', 'q',  'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
voc=['a','i','u','e','e']
hy=random.choice([0,1,2,3,4,5,6,7])
hx=random.choice([0,1,2,3,4,])

#present_word = ['acuh','amin','antah','']

def checkdb(txt,s):
    txt='db.txt'
    with open(txt,'r') as re:
        for a in re:
            if a == s:
                stat = True
            else:
                stat = False
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
    r=random.choice(hy)
    s=random.choice(hy)
    t=random.choice(hy)
    u=random.choice(hy)
    v=random.choice(hy)
    w=random.choice(hy)
    x=random.choice(hy)
    y=random.choice(hy)
    igotyou=c[r]+c[s]+c[t]+c[u]+c[v]+c[w]+c[x]+c[u]
    ig=list(igotyou)
    for itter in range(len(ig)):
        for items in ig:
            getfromitter=ig.count(ig[itter]) 
            if getfromitter == 1:                    
                return igotyou
            else:
                return gconso(conslist)
                
'''def gname7():
    pass
    x=random.choice([0,1,2,3,4,5,6,7])
    y=random.choice([0,1,2,3,4])
    name=a+b+const[y]+voc[y]+const[x]+voc[y]
    return str(name'''
    



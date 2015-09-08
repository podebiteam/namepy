'''
the simplicity
'''
import random
from namepyMod import generateName,checkdb,gvoc,gconslist,gconso



def main():
	g=gconslist()
	l=gconso(g) # get random consonant from gconsolist (g) and process with gconso to get ran conso
	voc=gvoc()
	for a in range(10):
		generateName('qwrth','aieuo',5)

if __name__ == '__main__':
	main()


'''
the simplicity
'''
import string,random,urllib2,re
from datetime import datetime
now=datetime.now()
print '##############################'
print '##      NAMING SYSTEM       ##'
print '##############################'
def name_meaning_present(name):
	pass #bugy,remove pass to know,if name mean is present
	global status
	status = ''
	url=urllib2.urlopen('http://www.morewords.com/word/'+name)
	read_data=url.read()
	if re.findall("No words found in this wordlist when searching for",read_data) != []:
		status = 'Present'
	else:
		status='Unpresent'
	print status

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
				region = 'Chile ('
			print region
		else:
			pass
	else:
		pass

def generate_first_name_len_5(list1,list2):
	'''generate random name with random alphabet
	'''
	#select random alphabet 
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
				res = 'match found'
			if final != None:
				print 'Current Name : {}'.format(final)
				print 'status : '+ res
				print '{} comes from --> '.format(final),region_detector(final)
			else:
				pass
def main():
	list1=list('jklhpmnb')
	list2=list('aiueo')
	generate_first_name_len_5(list1,list2)

if __name__ == '__main__':
	main()
	now2=datetime.now()
	print 'spent time', now2-now


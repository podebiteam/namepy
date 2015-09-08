
#-----------------------------------
#remove vocal letters!
#-----------------------------------
import string
words=string.lowercase
exception = ['a', 'i', 'u', 'e', 'o']
consonant=[]
for item in words:
    if item not in exception:
        consonant.append(item)

print consonant

'''
region detector
'''
# don't reinvent the wheel!

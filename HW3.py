# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:09:53 2017

@author: Zeeshan
"""
#18.

from nltk.corpus import gutenberg #import gutenberg
import nltk #
import re
fd=nltk.FreqDist([w for w in gutenberg.words('austen-emma.txt') if re.search('^[Ww]h.*',w) ])
#Reading austen-emma.txt word by word
#The regex used in this case is ‘^[Ww]h.*’ it checks whether a word starts with capital or small w,
#followed by h and then o or more single characters.
#FreqDist function will give us the frequency distribution
for m in fd: 
        print(m,":",fd[m])    
#Plotting the frequency distribution of words
fd.plot()


#19.
import os  #import os package
os.chdir("C:\Study\Python")  #Setting the current working directory
target = open("question19.txt", 'w')
#Opening the file in write mode, filehandle used is target
target.write("Zeeshan 45")
target.write("\n")
target.write("Ali 77")
target.write("\n")
target.write("Aloo 90")
target.write("\n")
target.write("baingan 22")
target.write("\n")
#Writing lines in file

#Closing the file handle
target.close()

#Reading lines of file
red=open("question19.txt").readlines()

a=[] #declaring empty list
for line in red:
    a.append((line.split(" ")))
#Appending elements in empty list after splitting on " "

#Replacing \n and converting into int
a[0][1]=int(re.sub(r"\n","",a[0][1]))  
a[1][1]=int(re.sub(r"\n","",a[1][1]))
a[2][1]=int(re.sub(r"\n","",a[2][1]))
a[3][1]=int(re.sub(r"\n","",a[3][1]))
#Printing the final list
print(a) 


#21.
from urllib import request
from bs4 import BeautifulSoup
import re
from nltk.corpus import words

def unknown(url):
    #Response from web page
    page= request.urlopen(url).read().decode('utf8') #read and decode UTF-8 format
    bs = BeautifulSoup(page).get_text()   #beautiful soup for web scraping
    corpWords = set(words.words()) #Corpus Dictionary words
    pg_words = re.findall(r'\b\w+', bs)  #Find all words starting with a boundary
    uniqueWords=[word for word in pg_words if word not in corpWords] #iterate through all html words
    #Finding words which are not present in corpus word dictionary
    print(set(uniqueWords)) #Print unique words from html that are not in dict

url1="http://www.nltk.org/"    
unknown(url1)        #Calling function with argument    

#23. 
import nltk
import re
import os
#	opening text file containing don't
os.chdir("C:\Study\Python")

f = open('trial.txt','w')
f.write("don't don't don't don't")
f.close()

f1 = open('trial.txt','r')
pal=f1.read()
#reading file
f1.close()
#regex to get groups of do and n't
zz = re.findall(r'\b(do)(n\'t)', pal)
print(zz)


#24.
import nltk
import re

#	reads in a text

f1 = "Sample noob for becoming a hacker. 1 for the  team, i love you let's rock YOLO Supra"

# lowercases the text
f1 = f1.lower()



def convertHacker(text):
	"""conversion  hAck3r"""
	new_text = []

	#initial pass subsitutes 8 for ate.
	z = re.compile(r'ate')
	text = z.sub('8', text) 

	# regex that searches through the text to find instances of the letters to be converted.
	z = re.compile(r'[eiols]|\.')


	# converts all the letters
	for w in text:
		if re.search(z, w):
			if w == 'e':
				w = '3'
			elif w == 'i':
				w = '1'
			elif w == 'o':
				w = '0'
			elif w == 's':
				w = '5'
			elif w == 'l':
				w = '|'
			elif w == '.':
				w = '5w33t!'
		new_text.extend(w)
	new_text = ''.join(new_text)

	# regex searching for word initial s.
	z = re.compile(r'\b5')
	ntext = z.sub('$', new_text)

	return ntext

text = convertHacker(f1)
print(text)

#27.
from random import choice

stringr = ''.join(list((choice("aehh ") for x in range(500))))
stringr = stringr.split(' ')
stringr = ''.join(stringr)
print(stringr)


#31.
saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']

length1 = [] #Declaring empty list
for i in saying:
	length1.append(len(i))   #Appending in list from original list
print(length1)

# list comprehension 
length2 = [len(i) for i in saying]
print(length2)

#32.
silly = 'newly formed bland ideas are inexpressible in an infuriating way'
#Declaring silly string

#a. Splitting silly
bland = silly.split(' ')

#Empty string
silly_word = ''

#b. Printing eoldrnnnna
for word in bland:
	silly_word += word[1]
print(silly_word)

#c.
new_bland = ' '.join(bland)
print(new_bland)
print(bland)

#d. silly in alphabetical order, one per line. 
bland = sorted(bland)
for w in bland:
	print(w)

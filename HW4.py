# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:28:19 2017

@author: Zeeshan
"""


#13
#Creating a word list of different words
word_list=['aaa','finish','loper','farhenieit']
#Declaring Viwels both in small and capital
f="aeiouAEIOU"
#Getting the maximum length out of all the words
dd=len(max(word_list, key=len))
#Declaring a two dimensional matrix of [max_length]  X [max_length] size of the word
word_vowels = [['' for z in range(dd)] for j in range(dd)]
#Initializing the matrix with ' '
print(word_vowels)
#Looping each word
for i in word_list:
    count=0    #Initializing counter
    l=len(i)   #length of word
    for v in i:     #Looping letter of word
        if v in f:  #if letter in vowels
            count=count+1   #Increase Counter
    print(l,count,i)    #Printing value for debugging
    word_vowels[l-1][count-1]=i    #we are doing -1 because the index are 0 to n-1
#Assigning to matrix, row is length of word and column is sum of vowel in word


print(word_vowels)    

#15
import nltk
#import nltk

#Declare empty list
li=[]
#Declare empty string
wor=''

#Check until user enters something
while(len(wor)==0):
    wor=input("Enter a Sentence : ")  #User input from terminal
    if(len(wor)!=0):    #Check the length of the string entered
        break           #if the length is greater than 0 for wor variable then break

li=wor.split(' ')   #split on the basis of space
x=len(li)           #number of words in list
z=nltk.FreqDist(li) #Frequency Distribution


print("No. of Words in sentence are :",x)  #Printing no. of words
print("Frequency Distribution\n")

for key in sorted(z):                   #Printing sorted 
    print("%s: %s"%(key, z[key]))       #Key and value pairs

#19
from nltk.corpus import wordnet as wn
#Importing nltk corpus wordnet

#Defining a function that returns the shortest path distance for each synset
def funcNew(a, b):
    disl = [(a.shortest_path_distance(syn), syn) for syn in b] #Calling shortest Distance 
    disl.sort() #sorting the list
    return disl  #returning the value

#Other Synset from which we want to compare distance
warp=['minke_whale.n.01', 'orca.n.01', 'novel.n.01', 'tortoise.n.01']
#Synsets for each string
b = [wn.synset(syn)  for syn in warp]
#Synset for 'right_whale.n.01'
a=wn.synset('right_whale.n.01')

#Calling the funcion which calculates the shortest distance and returns in sorted manner
funcNew(a, b)


#20
#Define a variable dupC
def dupC(st):
    print(st)  #Debugging print
    nw=st.split(" ")   #Splitting sentence on space
    nn=nltk.FreqDist(nw)   #Frequency Distribution
    length = len(set(nn))   #len of set
    j = list(nn.most_common(length))  #Getting the most_common
    j = [i[0] for i in j]
    print(j)

dupC("Z Z Z sha Na N Na p pop p")

        
#21
#Words 
words=['aaa','bbb','ccc']
#Vocablary list
vocab=['aaa','bbb','ddd','eee']
#Defining function which takes set difference and prints it
def diffJ(w,v):
    print(set(w).difference(v))
#Calling the function
diffJ(words,vocab)

#22
#
from operator import itemgetter
#words=['zss','eisos','voldo','poper','harakiri','ain','nebula']
words=['boil','afc','sack','jazz','fa']
#It is part of operator package 
#calling sorted function with ItemGetter
sorted(words, key=itemgetter(1))
sorted(words, key=itemgetter(-1))

#23


#list of words to test from    
words=['z','shan','jeep','vanguard','pop','faught']

#function lookup arguments trie and key
def lookup(trie,key):
    z=[x for x in trie if key in x #if key in trie
    print(z)   #Printing
#calling lookup function 
lookup(words,'van')


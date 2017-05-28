# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 03:26:41 2017

@author: Zeeshan
"""

#Q13
import nltk
from nltk.corpus import wordnet as wn
#importing nltk and wordnet
an=wn.all_synsets('n') #importing all nouns
anum=len(set(an))   #counting all nouns
anum    
#Nouns with No hyponyms or Hyponyms as 0  
nn=[w for w in wn.all_synsets('n') if len(w.hyponyms()) ==0] 
nnum=len(nn)
nnum
percentage=(nnum)/anum*100   #Calculating % of no hyponyms with all nouns
percentage
print("Percentage is "+str(percentage)) 


#Q14
#Function Supergloss accepting sysnet argument and return concatonated string
def supergloss(s):
    s_def=s.definition()
    hypo_def=s.hyponyms()
    listed=[]
    for w in hypo_def:
        listed.append(w.definition())
    hyper_def=s.hypernyms()
    for w in hyper_def:
        listed.append(w.definition())

    return s_def+str(listed)

#Calling functions
supergloss(wn.synset('car.n.01'))


#Q16
#Getting the lexical diversity of the categories in brown corpus
from nltk.corpus import brown
for z in nltk.corpus.brown.categories():
    l1 = len(set(w.lower() for w in brown.words(categories=z)))
    l2= len(brown.words(categories=z))
    diversity = l1/l2
    print (z, diversity)


#Q17
#Function to 50 most common words that are not stop words
from nltk.book import *
def common_words(text):
    stopwords = nltk.corpus.stopwords.words('english')
    ct = [w for w in text if w.lower() not in stopwords and w.isalpha()]
    return nltk.FreqDist(ct).most_common(50)

common_words(text1)


#Q18
#Function to avoid bigrams of stop words and print common bigrams
def common_bigrams(text):
    sw = nltk.corpus.stopwords.words('english')
    ct = [w for w in text if w.lower() not in sw and w.isalpha()]
    return FreqDist(nltk.bigrams(ct)).most_common(50)

common_bigrams(text1)


#Q20
#Function to check word freq 
def word_freq(word, se):
    from nltk.corpus import brown
    freq=0
    for w in brown.words(categories=se):
        if w==word:
            freq+=1
    return "Frequency "+word+" in "+se+" is "+str(freq)

#Call
word_freq("love", "belles_lettres")


#Q22
def hedge(text):
    counter=0
    list1=[]
    for w in text:
        counter+=1
        if counter%3==0:
            list1.append("like")
            list1.append(w)
        else:
            list1.append(w)
    return (list1)    

hedge(text1)

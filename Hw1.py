# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from nltk.book import *

#18.
#Adding list of sent
sentmy=sent1+sent2+sent3+sent4+sent5+sent6+sent7+sent8
#unique and sorted
sentmy2=sorted(set(sentmy))
#Counting Vocabulary
len(sentmy2)


#19.
#converting all words in lower from text1, getting distinct words and sorting them
len(sorted(set(w.lower() for w in text5)))

#Getting distinct words, changing them in lower case and then sorting them
len(sorted(w.lower() for w in set(text5)))


#20.
#This will check whether it is uppercase or not
"Zeeshan".isupper()

#This will just invert the result of islower function
not "Zeeshan".islower()


#21.
#This will extract last two words of text2
text2[-2:]


#22.
#Getting all four letter words
z=[w.lower() for w in text5 if len(w) == 4]
#Frequency Distribution
z1=FreqDist(z)
#Sorting based on values from high to low
sorted(z1.items(), key=lambda x:x[1], reverse=True)

#24.
#Ending with 'ize'
sorted(w for w in set(text6) if w.endswith('ize'))

#Containing 'z'
sorted(term for term in set(text6) if 'z' in term)

#Containing 'pt'
sorted(term for term in set(text6) if 'pt' in term)

#Containing first letter capital other letters as lowercase
sorted(item for item in set(text6) if item.istitle())

#25.
#Defining list sent
sent=['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

#Starting with 'sh'
[w for w in set(sent) if w.startswith('sh')]

#If word longer than four letters
[w for w in set(sent) if len(w)>4]



#26.
#It is summing up the length of all words of text1
sum(len(w) for w in text1)


sum(len(w) for w in text1)/len(text1)


#27.
#Defining function vocab_size
def vocab_size(text):
    return len(set([word.lower() for word in text]))

vocab_size(text1)

#28.
#Function to calculate word %
def percent(word, text):
    return 100 * text.count(word) / len(text)

#CAlling function
print(str(percent("the",text1))+'%')

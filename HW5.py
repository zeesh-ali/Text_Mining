# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:37:22 2017

@author: Zeeshan
"""
#15.1
import nltk



from nltk.corpus import brown
#import nltk corpus brown
noun={word for word, pos in brown.tagged_words() if pos.startswith('NN')}
#get all nouns with tag NN
nouns={word for word, pos in brown.tagged_words() if pos.startswith('NNS')}
#get all plurals with tag NNS
fnoun=nltk.FreqDist(noun)
#get Frequency distrubtion of nouns
fnouns=nltk.FreqDist(nouns)
#get Frequency distrubtion of nouns plural

#Loop through nouns
for wo in nouns:
    #string operation to derive singular from plural
    new_n=wo[:-1]
    #if the frequency of plural is more than singular    
    if(fnouns[wo]>fnoun[new_n]):
        print(wo)   #Print the plural if it has more freq than singular
        
#15.2
#Getting tagged words from brown corpus news category
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')   
#Getting nltk conditional frequency distribution of tags
data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_news_tagged)
z=0 #Initializing a counter
#looping through data variable
for word in sorted(data.conditions()):     
    #getting the tags for each word
    tags = [tag for (tag, _) in data[word].most_common()]
    #if the number of tags is greater than existing counter 
    if(z<len(tags)):
        z=len(tags) #update the counter with max no. of tags
        fr=(word, ' '.join(tags))     #store the word and its tag with most distinct tags
print(fr)   #print the words and its tags

#15.3
#Getting Frequency Distribution, from brown news category
mostTag = nltk.FreqDist(t for (w,t)  in  brown_news_tagged)
#Printing most common 
print (mostTag.most_common(20))

#15.4
#Noun Bigram
nounBigram =nltk.bigrams(t for (w,t)  in  brown_news_tagged)
#Freq Distribution, 
afterN = nltk.FreqDist(t1 for (t1,t2)  in  nounBigram if t2 == 'NOUN')
#Printing the nouns most commonly found after
print (afterN.most_common(20))


#18a.
#Calculating CFD for brown corpus
cfd = nltk.ConditionalFreqDist(brown.tagged_words())

#All conditions tags of from conditional Frequency distribution
cond = cfd.conditions()
#find single tag words
single_tags = [cond for cond in cond if len(cfd[cond]) == 1]
#Calculating proportion of assigned same part of speech tag or single tag
propSingle= len(single_tags) / len(cond)
#Printing proportion
print(propSingle)


#18b.
#Getting tagged words from brown corpus news category
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')   
#Getting nltk conditional frequency distribution of tags
data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_news_tagged)
#looping through data variable
for word in sorted(data.conditions()):     
    #getting the tags for each word
    tags = [tag for (tag, _) in data[word].most_common()]
    #Checking if the word is coming for more than two tags
    if(len(tags)>2):
        fr=(word, ' '.join(tags))     #Join all the tags
        print(fr)       #printing ambiguous word

#18c.
total=len(brown.tagged_words())
data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown.tagged_words())
ambiguous=0 #Initializing a counter
#looping through data variable
for word in sorted(data.conditions()):     
    #getting the tags for each word
    tags = [tag for (tag, _) in data[word].most_common()]
    #Checking if the word is coming for more than two tags
    if(len(tags)>2):
        ambiguous=ambiguous+1
#Get the percentage of ambiguous words        
ambiguous=(ambiguous/total)*100
#Printing the ambiguous words
print(ambiguous)


#21.

hal = brown.tagged_words(tagset='universal')
#getting tagged words
hal_bigrams = list(nltk.bigrams(hal))
#getting bigrams from tagged words
for bi in hal_bigrams:
    #For each bigrams
	zig = [list(d) for d in zip(*bi)]
    #if the word is adore, love, prefer or like and it is verb which follows adjective
	if zig[0][1] in ['adore', 'love', 'prefer', 'like'] and zig[1][1] == 'VERB' and zig[1][0] == 'ADV':
		print(zig[0][0],zig[0][1])   #Printing the ADV and VERB word
        
#22.
import nltk
#importing nltk related packages
from nltk.corpus import brown

patterns = [
	(r'.*ed$', 'VBD'), # verb ending with ed simple past 
	(r'.*ing$', 'VBG'), # verb ending in 'ing'
	(r'.*s$', 'NNS'), # plural nouns
	(r'.*\'s', 'NN$'), # possessive, aporstrophe s
	(r'.*', 'NN') #   #noun
]

#getting brown sentences from news category
bs = brown.sents(categories='news')
#regular expression for taggers to search for above patters
regexp_tagger = nltk.RegexpTagger(patterns)
#Printing the matching pattern from brown sentences
print(regexp_tagger.tag(bs[1]))

#26.

def perf(cfd, wl):
    # Input arguments conditional freq and worlist

    # goes through every word iun the wordlist and returns a dictionary
    zz = dict((word, cfd[word].max()) for word in wl)

    #Provide the above assigned variable and also there is default noun tagger

    bt = nltk.UnigramTagger(model=zz, backoff=nltk.DefaultTagger('NN'))

    # bt.evaluate for brown sentences is returned
    return bt.evaluate(brown.tagged_sents(categories='news'))

def disp():
    import pylab
    #importinh pylab
    # pulls in a frequency distribution 
    wf = nltk.FreqDist(brown.words(categories='news')).most_common()
    # sequentially orders the words by frequency
    wfreq = [w for (w, _) in wf]
    # makes a cfd  on the words and tags
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))

    # returns a list of scales
    sizes = 2 ** pylab.arange(15)

    # for every size, evaluate a baseline tagger based on a training set of that size. 
    perfs = [perf(cfd, wfreq[:size]) for size in sizes]
    #Plotting 
    pylab.plot(sizes, perfs, '-bo')

    # sets all label for axis
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

disp()  #Calling function


#29.
bts = brown.tagged_sents(categories='news')
#Getting brown sentences

size = int(len(bts) * 0.9)
#training data 90%
train_sents = bts[:size]
#testing data
test_sents = bts[size:]
#Noun as default tagger
t0 = nltk.DefaultTagger('NN')
#Unigran tagger  with backoff option as default tagger
t1=nltk.UnigramTagger(train_sents, backoff=t0)
#Bigram tagger training data
bigram_tagger = nltk.BigramTagger(train_sents)
#bigram seen data
bigram_tagger.tag(bts[2007])
#bigram unseen data
unseen_sent = bts[4203]
#bigram unseen data
bigram_tagger.tag(unseen_sent)
#bigram training data
bitag1=nltk.BigramTagger(train_sents)
#Bigram with cutoff=2 option will ignore the words unless it is atleast 2 times, 
#so those data that are in training data and  seen once only will be not recognized
bitag2=nltk.BigramTagger(train_sents, cutoff=2)
#Evaluate with cutoff=2
bitag2.evaluate(test_sents)
#Evaluate without cutoff=2
bitag1.evaluate(test_sents)

#30
#Get sentences from brown 
sentences = brown.tagged_sents(categories="news")
#Frequency ditribution of words
freqW = nltk.FreqDist(brown.words())
#Counter for sentences
n1 = []
#For loop of sentences
for t in sentences:
    n2 = []  #couter for word
    #Couter for each word
    for wad in t:
        #if word freq is 1 then assign UNK
        if freqW[wad]==1:
            n2.append(("UNK", wad[1]))
        else:
            #else assign normal word and its tag
            n2.append((wad[0], wad[1]))
    #Append the n2 words in n1 sentence counter        
    n1.append(n2)
#Training data 
size = int(len(n1) * 0.9)
train = n1[:size]
#testing data
test = n1[size:]

t0 = nltk.DefaultTagger('NN')      #Noun default tagger
t1 = nltk.UnigramTagger(train, backoff=t0)   #unigram tagger
t2 = nltk.BigramTagger(train, backoff=t1)   #bigram tagger
#Printing the evaluation
print("Default : ",t0.evaluate(test),"\n","Unigram : " ,t1.evaluate(test),"\n","Bigram : ", t2.evaluate(test),"\n")
        

#31
#Define perf function which taked cond freq dist and word list as input arg
def perf2(cfd, wl):
    #assign word and cfd as dictionary to variable
    zz = dict((word, cfd[word].max()) for word in wl)
    bt = nltk.UnigramTagger(model=zz, backoff=nltk.DefaultTagger('NN'))
    return bt.evaluate(brown.tagged_sents(categories='news'))
#define disp function to plot
def disp2():
        import pylab  #import pylab
        word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()  #word freq
        words_by_freq = [w for (w, _) in word_freqs]    #each word freq
        cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))   #conditional freq for news category
        sizes = 2 ** pylab.arange(15)   #pylabe arrange labels distance
        perfs = [perf2(cfd, words_by_freq[:size]) for size in sizes]  #loop through sizes
        pylab.semilogx(sizes, perfs, '-bo')      
        #Assign label of axis
        pylab.title('Lookup Tagger Performance with Varying Model Size')
        pylab.xlabel('Model Size')
        pylab.ylabel('Performance')
        pylab.show()   #Plot diagram

disp2()  #Call disp function

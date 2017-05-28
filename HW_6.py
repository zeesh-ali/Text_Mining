# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 03:36:27 2017

@author: Zeeshan
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 19:42:54 2017

@author: Zeeshan
"""
#2
import nltk
#import nltk
#Define function to return last letter of the word as a feature
def gender_features1(word):
    return {'last_letter': word[-1]}

#Import names
from nltk.corpus import names
#get names labelled as male and female
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +[(name, 'female') for name in names.words('female.txt')])
import random   #random shuffle
random.shuffle(labeled_names)

#training name 1001 till last
train_names = labeled_names[1000:]
#Dev test second 500 names ranging from 501 to 1000 names
devtest_names = labeled_names[500:1000]
#test names first 500 names
test_names = labeled_names[:500]
#Get train_set which has feature and gender for each name 	
train_set = [(gender_features1(n), gender) for (n, gender) in train_names]
#Get devtest_set which has feature and gender for each name
devtest_set = [(gender_features1(n), gender) for (n, gender) in devtest_names]
#Get test_set which has feature and gender for each name
test_set = [(gender_features1(n), gender) for (n, gender) in test_names]
#Train NaiveBayes classifier on train_set
classifier = nltk.NaiveBayesClassifier.train(train_set)
#print accuracy on dev_test
print(nltk.classify.accuracy(classifier, devtest_set))

#Define a function which uses last two letters that is it has more features than the last function
def gender_features2(word):
     return {'suffix1': word[-1:],'suffix2': word[-2:]}
#Divide train,dev test and test set same as above but using gender_features2 function
train_set = [(gender_features2(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features2(n), gender) for (n, gender) in devtest_names]
test_set = [(gender_features2(n), gender) for (n, gender) in test_names]
#training naivebayes classifier on the train set
classifier = nltk.NaiveBayesClassifier.train(train_set)
#print accuracy on dev test
print(nltk.classify.accuracy(classifier, devtest_set))
#Increase in classification accuracy
print(nltk.classify.accuracy(classifier, test_set))
#####################################

#3
#importing senseval package
from nltk.corpus import senseval
#getting instance of interest.pos, senseval has four different instance
instances = senseval.instances('interest.pos')
#getting 10% of the instances in size variable
size = int(len(instances) * 0.1)
#Using size variable first 10% i.e. 236 in train_set and rest of the 90% in train_set
train_set, test_set = instances[size:], instances[:size]
#train naivebayes on train_set
classifier = nltk.NaiveBayesClassifier.train(train_set)
#Defining a function to return sense feature
def sense_features(left,word,right):
     return {'prefix': left[-1:]}
#Since senseval objects are not iterateable directly
#We will use below method to iterate on it and create training and then testing set
train=[]   #declare train variable
#For each train_Set
for inst in train_set:
   p = inst.position
   left = ' '.join(w for (w,t) in inst.context[p-2:p])
   word = ' '.join(w for (w,t) in inst.context[p:p+1])
   right = ' '.join(w for (w,t) in inst.context[p+1:p+3])
   senses = ' '.join(inst.senses)
   #print((left, word, right, senses))
   l=sense_features(left,word,right)
   train.append((l,senses))  #append left last letter and sense to train
#Training NaiveBayes Classifier on train 
classifier = nltk.NaiveBayesClassifier.train(train)

test=[]  #Declare test variable
#Iterating over senseval test_set to get left word and right   
for inst in test_set:
   p = inst.position
   left = ' '.join(w for (w,t) in inst.context[p-2:p])
   word = ' '.join(w for (w,t) in inst.context[p:p+1])
   right = ' '.join(w for (w,t) in inst.context[p+1:p+3])
   senses = ' '.join(inst.senses)
   #print((left, word, right, senses))
   l=sense_features(left,word,right)
   test.append((l,senses)) #append left last letter and sense to test

#accuracy of the classifier on test set
print(nltk.classify.accuracy(classifier, test))


#########################################

#4
#import movie_reviews 	
from nltk.corpus import movie_reviews
#get category and fileid in documents
documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]
random.shuffle(documents) #random shuffle
#Frequency distribution of movie review words
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
#first 2000 in word_features variable
word_features = list(all_words)[:2000]
#function to return contained words as feature
def document_features(document): 
    document_words = set(document) 
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features
#getting document features in a feature set variable
featuresets = [(document_features(d), c) for (d,c) in documents]
#training and testing split
train_set, test_set = featuresets[100:], featuresets[:100]
#Train naive bayes classifier on train_set
classifier = nltk.NaiveBayesClassifier.train(train_set)
#print the accuracy on test_set
print(nltk.classify.accuracy(classifier, test_set))
#30 most informative features
classifier.show_most_informative_features(30)



###############################################
#5
#Training data , dev test and testing data
train_names = labeled_names[1000:]
devtest_names = labeled_names[500:1000]
test_names = labeled_names[:500]
#Defining gender features function
def gender_features(word):
     return {'suffix1': word[-1:],'suffix2': word[-2:]}

#Spltting in training, dev test and test set
train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
test_set = [(gender_features(n), gender) for (n, gender) in test_names]


#Naive Bayes CLassifier training
classifier = nltk.NaiveBayesClassifier.train(train_set)
#Decision Tree Training
classifier2 = nltk.DecisionTreeClassifier.train(train_set)
#Maximum Entropy Training
classifier3=nltk.classify.MaxentClassifier.train(train_set)

#Naive Baise
print("Naive Bayes")
print("dev_test",nltk.classify.accuracy(classifier, devtest_set))
print("test",nltk.classify.accuracy(classifier, test_set))
print("==================")
#Decision Tree
print("Decision Tree")
print("dev_test",nltk.classify.accuracy(classifier2, devtest_set))
print("test",nltk.classify.accuracy(classifier2, test_set))
print("==================")
#Maximum Entropy
print("Max Entropy")
print("dev_test",nltk.classify.accuracy(classifier3, test_set))
print("test",nltk.classify.accuracy(classifier3, test_set))
print("==================")

####################################
#6
import nltk  #import nltk
#returninga feature
def d_feature(w):
    return {'left': w[-1:]}
#Train_words on correct usage
train_words=['strong sales','powerful chip']
#All combinations of these four
words_all=['strong chip','strong sales','powerful chip','powerful sales']

train_words1=[] #Train words variable
#Preprocessing data before we can use it for feaure extraction
for line in train_words:
    f1,f2=line.split(' ')
    train_words1.append((f1,f2))


all_words1=[]  #All words variable
#Preprocessing data before we can use it for feaure extraction
for line in words_all:
    f1,f2=line.split(' ')
    all_words1.append((f1,f2))
#All set having feature and word
all_set=[(d_feature(n), wor) for (n, wor) in all_words1]
#Train set having feature and word
tr_set=[(d_feature(n), wor) for (n, wor) in train_words1]
#Traing classifier
classifier = nltk.NaiveBayesClassifier.train(tr_set)
#Here it will only classify correct combination that;s why 0.5 accuracy
print(nltk.classify.accuracy(classifier, all_set))


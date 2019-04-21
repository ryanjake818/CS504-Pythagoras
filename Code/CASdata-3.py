#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:01:57 2019

@author: administrator
"""

import nltk
nltk.download()
import os
from nltk import word_tokenize
from nltk import punctuation
import string

cwd = os.getcwd()
cwd
os.chdir("/media/sf_Project")
f = open('CASdata - words.txt')

d = f.read()
print(d)

import re
data = re.sub('\W+',' ', d)
data

#tokenize the data and convert all words to lowercase
word = nltk.word_tokenize(data)
word
word = [w.lower() for w in word]

#frequency distribution of all occurrences in the data file
freqdist = nltk.FreqDist(word)
freqdist
print(freqdist.most_common(25))
freqdist.plot(25)

#remove stop words
from nltk.corpus import stopwords
filtered_word = [words for words in word if words not in stopwords.words('english')]
print(filtered_word) 

#remove punctuation (if a character is not alphabetical)
wordsonly = [words for words in word if words.isalpha()]
wordsonly

#remove identifier words, ie: you, I, me, myself, etc
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in wordsonly if not w in stop_words]
print(words)

#remove all words and phrases that we searched with our hashtags
new_stopwords = ['loriloughlin', 'college', 'utaustin', 'collegescam', 'student', 'students', 'twitter', 'usc', 'pic', 'yale', 'com', 'https', 'http', 'ucla', 'stanford', 'collegecheatingscandal', 'collegeadmissionsscandal' ,'www', 'admissions', 'get', 'georgetown', 'ly', 'collegeadmissionscandal']
new_stopwords_list = stop_words.union(new_stopwords)
final_words = [w for w in words if not w in new_stopwords]

print(final_words)
 
#frequency distribution of words related to biking - I left in the option "None" because it was a valid review of no injuries
freqdistfilter = nltk.FreqDist(final_words)
freqdistfilter
print(freqdistfilter.most_common(25))
freqdistfilter.plot(25)

#BEFORE ANALYSIS
fB = open('CASdata - Before.txt')
dB = fB.read()
print(dB)

Bdata = re.sub('\W+', ' ', dB)
Bdata

Bword = nltk.word_tokenize(Bdata)
Bword

Bword = [w.lower() for w in Bword]
Bfiltered_word = [Bwords for Bwords in Bword if Bwords not in stopwords.words('english')]
print(Bfiltered_word) 

Bwordsonly = [Bwords for Bwords in Bword if Bwords.isalpha()]
Bwordsonly

stop_words = set(stopwords.words('english'))
Bwords = [w for w in Bwordsonly if not w in stop_words]
print(Bwords)

new_stopwords = ['loriloughlin', 'college', 'utaustin', 'collegescam', 'student', 'students', 'twitter', 'usc', 'pic', 'yale', 'com', 'https', 'http', 'ucla', 'stanford', 'collegecheatingscandal', 'collegeadmissionsscandal' ,'www', 'admissions', 'get', 'georgetown', 'ly', 'collegeadmissionscandal']
new_stopwords_list = stop_words.union(new_stopwords)
Bfinal_words = [w for w in Bwords if not w in new_stopwords]
print(Bfinal_words)

Bfreqdistfilter = nltk.FreqDist(Bfinal_words)
Bfreqdistfilter
print(Bfreqdistfilter.most_common(25))
Bfreqdistfilter.plot(25)


#AFTER ANALYSIS
fA = open('CASdata - After.txt')
dA = fA.read()
print(dA)

Adata = re.sub('\W+', ' ', dA)
Adata

Aword = nltk.word_tokenize(Adata)
Aword

Aword = [w.lower() for w in Aword]
Afiltered_word = [Awords for Awords in Aword if Awords not in stopwords.words('english')]
print(Afiltered_word) 

Awordsonly = [Awords for Awords in Aword if Awords.isalpha()]
Awordsonly

stop_words = set(stopwords.words('english'))
Awords = [w for w in Awordsonly if not w in stop_words]
print(Awords)

new_stopwords = ['html', 'loriloughlin', 'college', 'utaustin', 'collegescam', 'student', 'students', 'twitter', 'usc', 'pic', 'yale', 'com', 'https', 'http', 'ucla', 'stanford', 'collegecheatingscandal', 'collegeadmissionsscandal' ,'www', 'admissions', 'get', 'georgetown', 'ly', 'collegeadmissionscandal']
new_stopwords_list = stop_words.union(new_stopwords)
Afinal_words = [w for w in Awords if not w in new_stopwords]
print(Afinal_words)

Afreqdistfilter = nltk.FreqDist(Afinal_words)
Afreqdistfilter
print(Afreqdistfilter.most_common(25))
Afreqdistfilter.plot(25)

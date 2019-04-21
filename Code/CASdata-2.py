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
 
#frequency distribution of words related to biking - I left in the option "None" because it was a valid review of no injuries
freqdistfilter = nltk.FreqDist(words)
freqdistfilter
print(freqdistfilter.most_common(25))
freqdistfilter.plot(25)

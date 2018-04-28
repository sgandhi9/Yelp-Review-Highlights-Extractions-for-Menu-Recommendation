import nltk
from nltk.util import ngrams 
from nltk.tokenize import sent_tokenize
from nltk import load
from textblob import TextBlob, Word
from collections import Counter
import csv

'''
To further filter the review for users, we are using this code to create list of relavent noun words 
'''

f=open('C:/Users/ranji/Desktop/project 660/final/tips.txt')
fn=open('C:/Users/ranji/Desktop/project 660/final/nouns.txt','w')
text=f.read().strip()
f.close()
blob = TextBlob(text)

nouns = list()
for word, tag in blob.tags:
    if tag == 'NN':
        nouns.append(word.lemmatize())
nouns=[x for x in nouns if x != 'i']
fn.write(str(nouns))
freqNouns = Counter(nouns)
with open('C:/Users/ranji/Desktop/project 660/final/counter.csv','w') as csvfile:
    writer=csv.writer(csvfile,dialect='excel')
    for noun in nouns:
        if noun:
            writer.writerow([noun])
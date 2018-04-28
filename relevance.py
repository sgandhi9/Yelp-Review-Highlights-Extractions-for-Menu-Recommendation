from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging
from sklearn.preprocessing import StandardScaler
from pylab import rcParams
import csv

'''
We are using this code to find the relavence of words from filtered reviews with noun phrases
'''

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
f=open("relevant.txt",'w')
# train word2vec model on the list
model0 = Word2Vec(LineSentence("C:/Users/ranji/Desktop/project 660/final/counter.csv"), size=10, window=2, min_count=1, workers=4)
list1=model0.most_similar('food', topn=10)
print((list1[0]))
with open("C:/Users/ranji/Desktop/project 660/final/relevant.csv","w") as result:
    wr = csv.writer(result,dialect="excel")
    for each in list1:
        if each:
            wr.writerow(each)
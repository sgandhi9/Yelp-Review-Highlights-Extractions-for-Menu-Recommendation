import unicodedata
from lxml import etree
import requests
from lxml import html
import numpy as np
import io
import pandas as pd
import re
import nltk

'''
This code is used to create specific words from the relevent tips which will be used for recommendation for the customers and restaurant owner 
'''

g=open("C:/Users/Shailesh Gandhi/Desktop/final_tips.txt",'w')
file = open('C:/Users/Shailesh Gandhi/Desktop/BIA FINAL 660/relevant.csv')
column_1st = pd.read_csv(file, sep=',',header=0,usecols=[0])
listw=column_1st['words'].values.tolist()
content = []
with open("C:/Users/Shailesh Gandhi/Desktop/BIA FINAL 660/tips.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
unique={}                             
for sent in content:
    for word in listw:
        if word in sent:
            unique[word] = sent
                      
for i in unique:
    g.write(str(i)+": "+unique[i]+"\n")  
g.close()
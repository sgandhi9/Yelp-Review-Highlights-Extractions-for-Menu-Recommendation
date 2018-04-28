from lxml import etree
import requests
from lxml import html
import string
from nltk.tokenize.moses import MosesDetokenizer
import nltk

'''
In this piece of code, we have used LXML for extracting the review from the page url we exctracted earlier
'''

root = etree.Element('html')
root.tag
etree.SubElement(root,'head')
etree.SubElement(root,'body')
print(etree.tostring(root))

path='C:\\Users\\ranji\\Desktop\\project 660\\List_NY.txt'    #Reading the file from which the restaurants names are taken to search in Yelp and Scrape the reviews
fin=open(path)
f = open("C:\\Users\\ranji\\Desktop\\project 660\\List_NY_highlights.txt","w")
for line in fin:                                              #For each name of restaurant in the List
                words = line.lower().strip()                     
                restraunt_name=words
                url='https://www.yelp.com'+restraunt_name
                page= requests.get(url)
                html_content = html.fromstring(page.content)
                for i in range(1,4):
                    x=[]
                    y=html_content.xpath('//*[@id="super-container"]/div/div/div[1]/div[1]/div[1]/ul/li['+str(i)+']/div[2]/p/a[1]/text()')
                    z=html_content.xpath('//*[@id="super-container"]/div/div/div[1]/div[1]/div[1]/ul/li['+str(i)+']/div[2]/p/text()')
                    
                    z=str(z).replace('[','').replace(']','')
                    z=str(z).replace("', '\n    '","")
                    z=z.replace("'", "")
                    
                    x = nltk.word_tokenize(z)
                    x = [''.join(c for c in s if c not in string.punctuation) for s in x]
                    x = [s for s in x if s]
                    
                    x1= list(filter(('n').__ne__, x))    
                    size = len(x1)
                    x1 = x1[1:size-2]
                    detokenizer = MosesDetokenizer()
                    list1=detokenizer.detokenize(x1, return_str=True)
                    list1.strip()
                    list1=list1[1:-1]
                    f.write("%s\n"%list1)
f.close()

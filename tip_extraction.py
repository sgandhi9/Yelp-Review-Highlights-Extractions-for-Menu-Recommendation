import re
'''
This code is used to extract the tips from the raw review using n-grams
'''

f=open("C:/Users/ranji/Desktop/project 660/final/tips.txt",'w')
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for sentence in lex_conn:
        newLex.add(sentence.strip())# remember to strip to remove the lin-change character
    lex_conn.close()
    return newLex

searchfile = open("C:/Users/ranji/Desktop/project 660/final/rosies-new-york.txt")
file_lex=loadLexicon('C:/Users/ranji/Desktop/project 660/final/List_lexicon_of_expressions.txt')
text=searchfile.read().lower()
sentences = text.split('.')

for sent in sentences:
    #print(sent)
    sent=sent.lower().strip()
    sent=re.sub("[^a-zA-Z0-9|?|.|,|!|-|:|;|&|@|_|/|>|<|#|$|']",' ',sent)
    words=sent.split(' ')
    unique=set()
    for word in words:
        if word in file_lex:
            unique.add(sent)
    for i in unique:   
        f.write(str(i)+" "+"\n")
f.close()
searchfile.close()
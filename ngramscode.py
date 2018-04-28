import nltk
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize
from nltk import load

"""
The script includes the following pre-processing steps for text:
- Sentence Splitting
- Term Tokenization
- Ngrams
- POS tagging

The run function includes all 2grams of the form: <ADVERB> <ADJECTIVE>

"""

def getAdvAdjTwograms(terms,adj,adv): # return all the 'adv adj' twograms
    result=[]
    twograms = ngrams(terms,2)  
    for tg in twograms:  
        if tg[0] in adv and tg[1] in adj: # if the 2gram is a an adverb followed by an adjective
            result.append(tg)
    return result

def getAdjOnegrams(terms,adj): # return all the 'adj' unigrams
    resultadj=[]
    onegrams = ngrams(terms,1) #compute unigrams
    for og in onegrams:  
        if og[0] in adj: # if the unigram is a an adjective
            resultadj.append(og[0])
    return resultadj

def getPOSterms(terms,POStags,tagger): # return all the terms that belong to a specific POS type
    tagged_terms=tagger.tag(terms) # do POS tagging on the tokenized sentence
    POSterms={}
    for tag in POStags:POSterms[tag]=set()
    for pair in tagged_terms:     #for each tagged term
        for tag in POStags:     # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])
    return POSterms

def run1(fpath):
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)
    f=open(fpath)
    text=f.read().strip()
    f.close()
    sentences=sent_tokenize(text)
    print ('NUMBER OF SENTENCES: ',len(sentences))
    adjAfterAdv=[]
    for sentence in sentences:
        terms = nltk.word_tokenize(sentence)   
        POStags=['JJ','RB'] # POS tags of interest 		
        POSterms=getPOSterms(terms,POStags,tagger)
        adjectives=POSterms['JJ']
        adverbs=POSterms['RB']
        adjAfterAdv+=getAdvAdjTwograms(terms, adjectives, adverbs)
        newadjAfterAdv=set(adjAfterAdv)
    return newadjAfterAdv

def run2(fpath):
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)
    f=open(fpath)
    text=f.read().strip()
    f.close()
    sentences=sent_tokenize(text)
    print ('NUMBER OF SENTENCES: ',len(sentences))
    adjAfterAdv=[]
    for sentence in sentences:
        terms = nltk.word_tokenize(sentence)   
        POStags=['JJ','RB'] # POS tags of interest 		
        POSterms=getPOSterms(terms,POStags,tagger)
        adjectives=POSterms['JJ']
        adjAfterAdv+=getAdjOnegrams(terms, adjectives)
        newadjAfterAdv=set(adjAfterAdv)	
    return newadjAfterAdv

if __name__=='__main__':
    run1=run1('List_NY_highlights.txt')
    run2=run2('List_NY_highlights.txt')
    f = open("C:\\Users\\ranji\\Desktop\\project 660\\List_lexicon_of_expressions.txt","w")
    for elem in run1:
        for elemlist in elem:
            f.write(str(elemlist)+" ")
        f.write("\n")
    for elem in run2:
        f.write("\n"+str(elem))
    f.close()




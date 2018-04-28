import nltk
from nltk.corpus import stopwords

'''
This code is final step for recognizing the sentiment of the unique tips.
'''
def tokenize(str):
        text = str.lower()
        pattern = r'[a-z]+[a-z\-\.]*'
        tokens = nltk.regexp_tokenize(text, pattern) 
        return tokens
    
class Text_Analyzer(object):
    def _init_(self, input_file):
        self.input = input_file

    def sentiment_analysis(self):
        with open(self.input) as f:
            line=f.readlines()
            line = [line.rstrip('\n') for line in line] 
            for tip in line:
                print(tip)
                tokens = tokenize(str(tip))
                stop_words = stopwords.words('english')
                filtered_tokens=[token for token in tokens if token not in stop_words] 
                
                with open("positive-words.txt", 'r') as  value:
                    positive_word = [line.strip() for line in value]
                positive_tokens = [token for token in filtered_tokens if token in positive_word]
                with open("negative-words.txt", 'r') as  value:
                    negative_word = [line.strip() for line in value] 
                negative_tokens = [token for token in filtered_tokens if token in negative_word]
           
                if len(positive_tokens)>len(negative_tokens):
                    response = "positive"
                if len(positive_tokens)<len(negative_tokens):
                     response="negative"
                if len(positive_tokens)==len(negative_tokens):
                     response="neutral"    
                print("The tip is:",str(response))
            return response

if __name__ == "__main__":  
    response = Text_Analyzer("final_tips.txt")
    sentiment= response.sentiment_analysis()
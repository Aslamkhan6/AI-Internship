import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class Preprocessor:
    nltk.download("wordnet")
    nltk.download("punkt")
    nltk.download("stopwords")
    lemmatizer = WordNetLemmatizer()
    def __init__(self,text):
        self.text = text
       



    #remove the  extra spaces 
    def lowerCase(self):
        self.text = self.text.lower()
        return self.text

    #remove punctuation
    def removePunctation(self):
         self.text = re.sub(r"[^\w\s]", "", self.text)
         return self.text


   # remove number
    def removeNumber(self):
       self.text = re.sub(r'\d+', '', self.text) 
       return self.text   


# remove extra space
    def  removeSpace(self):
         self.text = " ".join(self.text.split())  
         return self.text 

    #tokanization
    def tokanization(self):
        self.text = word_tokenize(self.text)
        return self.text     


    def removeStopWord(self):
         remsttext = []
         stop_word = stopwords.words("english")

         for remtxt in self.text:
             if remtxt not in stop_word:
                 remsttext.append(remtxt)

         self.text = remsttext
         return self.text

    def lemmatize(self):
        lemtxt = []

        for text in self.text:
            lemtxt.append(
            self.lemmatizer.lemmatize(text)
        )

        self.text = lemtxt
        return self.text

    def preprocessor(self):
      
       self.lowerCase() 
       self.removePunctation()
       self.removeNumber()  
       self.removeSpace()
       self.tokanization()
       self.removeStopWord()
       self.lemmatize()
       return self.text
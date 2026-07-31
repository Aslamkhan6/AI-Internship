
import re
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources only if they are missing
try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    
    nltk.download("wordnet")
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")


class Preprocessor:

    lemmatizer = WordNetLemmatizer()

    def __init__(self, text):
        self.text = text

    # Convert text to lowercase
    def lowerCase(self):
        self.text = self.text.lower()
        return self.text

    # Remove punctuation
    def removePunctation(self):
        self.text = re.sub(r"[^\w\s]", "", self.text)
        return self.text

    # Remove numbers
    def removeNumber(self):
        self.text = re.sub(r"\d+", "", self.text)
        return self.text

    # Remove extra spaces
    def removeSpace(self):
        self.text = " ".join(self.text.split())
        return self.text

    # Tokenization
    def tokanization(self):
        self.text = wordpunct_tokenize(self.text)
        return self.text

    # Remove stop words
    def removeStopWord(self):
        remsttext = []
        stop_word = stopwords.words("english")

        for remtxt in self.text:
            if remtxt not in stop_word:
                remsttext.append(remtxt)

        self.text = remsttext
        return self.text

    # Lemmatization
    def lemmatize(self):
        lemtxt = []

        for text in self.text:
            lemtxt.append(
                self.lemmatizer.lemmatize(text)
            )

        self.text = lemtxt
        return self.text

    # Complete preprocessing pipeline
    def preprocess(self):

        self.lowerCase()
        self.removePunctation()
        self.removeNumber()
        self.removeSpace()
        self.tokanization()
        self.removeStopWord()
        self.lemmatize()

        return self.text
import re
import string
import nltk

from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# ==========================================
# Download Required NLTK Data
# ==========================================

nltk.download("wordnet", quiet=True)
nltk.download("stopwords", quiet=True)


class Preprocessor:

    # Create once for better performance
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))

    def __init__(self, text):

        self.text = str(text)

    # ==========================================
    # Convert to Lowercase
    # ==========================================

    def lowerCase(self):

        self.text = self.text.lower()

        return self.text

    # ==========================================
    # Remove URLs
    # ==========================================

    def removeURL(self):

        self.text = re.sub(r"http\S+|www\S+|https\S+", "", self.text)

        return self.text

    # ==========================================
    # Remove HTML Tags
    # ==========================================

    def removeHTML(self):

        self.text = re.sub(r"<.*?>", "", self.text)

        return self.text

    # ==========================================
    # Remove Punctuation
    # ==========================================

    def removePunctuation(self):

        self.text = self.text.translate(
            str.maketrans("", "", string.punctuation)
        )

        return self.text

    # ==========================================
    # Remove Numbers
    # ==========================================

    def removeNumbers(self):

        self.text = re.sub(r"\d+", "", self.text)

        return self.text

    # ==========================================
    # Remove Extra Spaces
    # ==========================================

    def removeSpaces(self):

        self.text = " ".join(self.text.split())

        return self.text

    # ==========================================
    # Tokenization
    # ==========================================

    def tokenize(self):

        self.text = wordpunct_tokenize(self.text)

        return self.text

    # ==========================================
    # Remove Stopwords
    # ==========================================

    def removeStopWords(self):

        self.text = [

            word

            for word in self.text

            if word not in self.stop_words

        ]

        return self.text

    # ==========================================
    # Lemmatization
    # ==========================================

    def lemmatize(self):

        self.text = [

            self.lemmatizer.lemmatize(word)

            for word in self.text

        ]

        return self.text

    # ==========================================
    # Complete Preprocessing Pipeline
    # ==========================================

    def preprocess(self):

        self.lowerCase()

        self.removeURL()

        self.removeHTML()

        self.removePunctuation()

        self.removeNumbers()

        self.removeSpaces()

        self.tokenize()

        self.removeStopWords()

        self.lemmatize()

        return self.text
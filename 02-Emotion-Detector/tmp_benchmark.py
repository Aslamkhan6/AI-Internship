from src.datasets import Emotiondataset
from src.preproces import Preprocessor
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import nltk

nltk.download('wordnet', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

data = Emotiondataset().loaddata()
texts = data['text'].astype(str).tolist()
labels = data['emotion']

clean = []
for s in texts:
    clean.append(' '.join(Preprocessor(s).preprocess()))

X_train, X_test, y_train, y_test = train_test_split(clean, labels, test_size=0.2, random_state=42)

for name, model in [
    ('MultinomialNB', MultinomialNB()),
    ('LogReg', LogisticRegression(max_iter=5000)),
    ('LinearSVC', LinearSVC()),
]:
    vec = TfidfVectorizer(ngram_range=(1, 2), min_df=1, sublinear_tf=True)
    Xtr = vec.fit_transform(X_train)
    Xte = vec.transform(X_test)
    clf = model
    clf.fit(Xtr, y_train)
    pred = clf.predict(Xte)
    print(name, accuracy_score(y_test, pred))

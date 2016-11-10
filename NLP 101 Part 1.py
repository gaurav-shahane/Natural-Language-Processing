
#This is the NLP Tutorial written for the NLP 101 session conducted for the student group 'Data Science Army' at UMD.

#This code contains code for HTML Parsing, Sentence and Word Tokinizing, Stopwords Removal,
#Stemming, Lemmatizing, and Frequency Distribution analysls.

# Gaurav Shahane, MIM (Data Analytics), UMD

import nltk
from bs4 import BeautifulSoup
from nltk import FreqDist

#reading html web page
import urllib.request as urlreq
url = "http://news.harvard.edu/gazette/story/2008/06/text-of-j-k-rowling-speech/"
text = urlreq.urlopen(url).read()
#print(text)

#html Parsing using BeautifulSoup
text_soup = BeautifulSoup(text, 'html.parser')
for script in text_soup(["script", "style"]):
    script.extract()
text = (text_soup.body.get_text())

#sentence tokenizing
text = text.replace("\n", " ") #Remove new lines denoted by '\n'
text = text.lower()
text_sent = nltk.tokenize.sent_tokenize(text)

#word tokenize
text_word = []
for sent in text_sent:
    text_word = text_word + (nltk.tokenize.wordpunct_tokenize(sent))

#remove punctuation marks
text_nopunct = [w for w in text_word if w.isalnum()]

# Stop Words Removal
stopwords = nltk.corpus.stopwords.words('english')
text_wo_stopwords = [word for word in text_nopunct if not word in stopwords]

# Stemming
from nltk.stem import PorterStemmer
porter = PorterStemmer()
text_stemmed = []
for w in text_wo_stopwords:
    text_stemmed.append(porter.stem(w))

#Lemmatizing

from nltk import WordNetLemmatizer
wordnet = WordNetLemmatizer()
text_lemma = []
for w in text_stemmed:
    text_lemma.append(wordnet.lemmatize(w))


#frequency distribution of the words
text_freq = FreqDist(text_lemma)
print(text_freq.most_common(50))
text_freq.plot(50)


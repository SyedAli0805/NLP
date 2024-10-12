from nltk.stem import PorterStemmer


import spacy
import textblob
from textblob import TextBlob

# NLTK Stemming 
# Stemming
# Through Porter Stemmer
ps = PorterStemmer()
word = ("civilization")
print("NLTK Stem Word for CIVILIZATION: ",ps.stem(word))

#spaCY doesn't contain any direct method for Stemming 


#textBLOB
textblob_words = TextBlob("I have a very good collection of books")
for word in textblob_words.words:
    print(word, word.stem())
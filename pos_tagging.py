import nltk
from nltk import word_tokenize

# Ensure the averaged_perceptron_tagger is downloaded
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt')  # Download tokenizer

text = "Hello everyone! Welcome to the course on Natural Language Processing."

# Tokenize the text
tokens = word_tokenize(text)

# Perform POS tagging
print("Parts of Speech: ", nltk.pos_tag(tokens))


#SPACT POS TAGGING
nlp = spacy.load("en_core_web_sm")  # Load the SpaCy model
doc = nlp(text)

for word in doc:
    print(word.text,  word.pos_)


#TextBLOB POS Tagging
text = TextBlob("Hello everyone! Welcome to the course 123. We are studying Natural Language Processing.")

for word,tag in text.tags:
    print(word, tag)
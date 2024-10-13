import spacy

#loading english model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

text = "After several attempts, Sarah finally solved the puzzle. Exhausted yet relieved, she smiled. 'Was it luck or skill?' she pondered, unsure. Nevertheless, her determination paid off, proving that perseverance, rather than luck, often leads to success."

filtered_text = []
stopwords = []

for word in nlp(text):
    if word.is_stop:
        stopwords.append(word)
    else:
        filtered_text.append(word)
print("Text after stopword removal: ",filtered_text)
print("\n Stopwords: ",stopwords)
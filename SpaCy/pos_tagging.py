import spacy

#loading english model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

text = "After several attempts, Sarah finally solved the puzzle. Exhausted yet relieved, she smiled. 'Was it luck or skill?' she pondered, unsure. Nevertheless, her determination paid off, proving that perseverance, rather than luck, often leads to success."

for word in nlp(text):
    print(word,"   ",word.pos_)
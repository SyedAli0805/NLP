from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer

text = "generalization"

ps = PorterStemmer()

tokenizer = RegexpTokenizer(r'\w+')

words = tokenizer.tokenize(text)
stem_words = []
for word in words:
    stem_words.append(ps.stem(word))

print("Original Words: ",words)
print("\nStem Words: ",stem_words)
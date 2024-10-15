from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer

text = "After several attempts, Sarah finally solved the puzzle. Exhausted yet relieved, she smiled. 'Was it luck or skill?' she pondered, unsure. Nevertheless, her determination paid off, proving that perseverance, rather than luck, often leads to success."

ps = PorterStemmer()

tokenizer = RegexpTokenizer(r'\w+')

words = tokenizer.tokenize(text)
stem_words = []
for word in words:
    stem_words.append(ps.stem(word))

print("Original Words: ",words)
print("\nStem Words: ",stem_words)
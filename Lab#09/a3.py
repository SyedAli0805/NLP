import random
from collections import defaultdict

# Sample corpus
text = "Nature is good. Nature is great. Nature is good and great.It is Fascinating and Humongous."
tokens = text.split()
bigrams = list(zip(tokens[:-1], tokens[1:]))

print("Bigrams:", bigrams)

# Build the bigram model
bigram_model = defaultdict(list)
for bigram in bigrams:
    bigram_model[bigram[0]].append(bigram[1])

# Text generation
current_word = "Nature"
generated_sentence = [current_word]

for _ in range(5):  # Generate 5 more words
    if current_word in bigram_model:
        next_word = random.choice(bigram_model[current_word])
        generated_sentence.append(next_word)
        current_word = next_word
    else:
        break  
print("Generated Sentence:", " ".join(generated_sentence))

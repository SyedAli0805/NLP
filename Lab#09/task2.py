import random
from collections import defaultdict

# Sample corpus
text = "Nature is good. Nature is great. Nature is good and great. It is Fascinating and Humongous."
tokens = text.split()
trigrams = list(zip(tokens[:-2], tokens[1:-1], tokens[2:]))

print("Trigrams:", trigrams)

# Build the trigram model
trigram_model = defaultdict(list)
for trigram in trigrams:
    trigram_model[(trigram[0], trigram[1])].append(trigram[2])

# Text generation
current_word = ("Nature", "is")  
generated_sentence = list(current_word)

for _ in range(10):  # Generate 5 more words
    if current_word in trigram_model:
        next_word = random.choice(trigram_model[current_word])
        generated_sentence.append(next_word)
        current_word = (current_word[1], next_word)  
    else:
        break  

print("Generated Sentence:", " ".join(generated_sentence))

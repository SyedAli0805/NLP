import spacy

# Load pre-trained model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Apple is looking at buying U.K. startup for $1 billion"

# Process text
doc = nlp(text)

# Display the entities in the text
for ent in doc.ents:
    print(ent.text, ent.label_)
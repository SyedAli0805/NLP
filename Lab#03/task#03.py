import spacy
from spacy import displacy

# Load the SpaCy English model
nlp = spacy.load("en_core_web_sm")

text = "Despite the heavy rain, the team continued working on the project, which they hoped to finish by the end of the week."

doc = nlp(text)

print("Dependency Parsing:")
for token in doc:
    print(f"{token.text} -> {token.dep_} (Head: {token.head.text})")

# Visualize the dependency parse tree in the console
displacy.render(doc, style="dep", jupyter=False, options={'bg': 'white'})

# Save the visualization to an HTML file
html = displacy.render(doc, style="dep", options={'bg': 'white'})
with open("dependency_parsing.html", "w", encoding='utf-8') as f:
    f.write(html)

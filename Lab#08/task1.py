from textblob import TextBlob
#Customize Spell Check
from spello.model import SpellCorrectionModel
#Customize Spell Check
sp = SpellCorrectionModel(language='en')
with open('D:\\Semester#07\\Natural-Language-Programming\\NLP-Labs\\Lab#08\\dataset\\corpus.csv', 'r')as file:
    data = file.readlines()
    data = [i.strip() for i in data]
sp.train(data)
print(sp.spell_correct('Deforestation and habbitat distruction threten the survival of countless spieces.'))
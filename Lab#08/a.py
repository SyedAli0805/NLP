from textblob import TextBlob
#Customize Spell Check
from spello.model import SpellCorrectionModel
#Example 1
tb = TextBlob('i want to play fotball')
print(tb.correct())
#Example 2 - Only correct 1 word
tb = TextBlob('i want to paly fotball')
print(tb.correct())
#Customize Spell Check
sp = SpellCorrectionModel(language='en')

with open('D:\\Semester#07\\Natural-Language-Programming\\NLP-Labs\\Lab#08\\dataset\\spam.csv', 'r')as file:
    data = file.readlines()
    data = [i.strip() for i in data]
sp.train(data)
print(sp.spell_correct('I want to gel sckool'))
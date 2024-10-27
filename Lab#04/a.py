import pandas as pd
import string
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

pd.set_option('display.max_columns',100)
df = pd.read_csv(r'D:\Semester#07\Natural-Language-Programming\NLP-Labs\Lab#04\datasets\spam.csv',encoding='latin-1')
df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
print(df.head())

df.rename(columns={'v1': 'label', 'v2': 'text'}, inplace=True)
print(df.head())

print(f'ham={len(df[df["label"]=="ham"])}')
print(f'spam={len(df[df["label"]=="spam"])}')

print(f'numbers of missing labels = {df["label"].isnull().sum()}')
print(f'numbers of missing sms = {df["text"].isnull().sum()}')


print(string.punctuation)

def remove_punctuation(text):
  return text.translate(str.maketrans('','',string.punctuation))
df['cleaned_SMS'] = df['text'].apply(lambda x: remove_punctuation(x))
print(df.head())


df['message_length'] = df['cleaned_SMS'].apply(lambda x: len(x))
print(df.head())

plt.figure(figsize=(6,4))
sns.countplot(x='label',data = df)
plt.title('spam vs ham')
plt.show()

plt.figure(figsize=(8,6))
df[df['label'] == 'ham']['message_length'].plot(kind='hist', bins=50, alpha=0.7, label='Ham',
color='blue')

df[df['label'] == 'spam']['message_length'].plot(kind='hist', bins=50, alpha=0.7, label='Spam',
color='red')
plt.title('Distribution of Message Lengths by Label')
plt.xlabel('Message Length')
plt.ylabel('Frequency')
plt.legend()
plt.show()

spam_words = ' '.join(df[df['label'] == 'spam']['text'])
spam_wc = WordCloud(width=600, height=400,
background_color='black').generate(spam_words)

plt.figure(figsize=(8,6))
plt.imshow(spam_wc, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Spam Messages')
plt.show()

ham_words = ' '.join(df[df['label'] == 'ham']['text'])
ham_wc = WordCloud(width=600, height=400, background_color='white').generate(ham_words)

plt.figure(figsize=(8,6))
plt.imshow(ham_wc, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Ham Messages')
plt.show()


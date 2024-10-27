import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

#reading dataset
df = pd.read_csv(r'D:\Semester#07\Natural-Language-Programming\NLP-Labs\Lab#04\datasets\disaster-tweets.csv',encoding='latin-1')
print(df.head())

#analyzing dataset
print(df.info())
print(df.isnull().sum())

#replacing null values
df['keyword'].fillna('Unknown', inplace=True)
df['location'].fillna('Unknown', inplace=True)

#checking and removing duplicates
df.drop_duplicates(inplace=True)

#remove all characters except alphabets and numbers
def remove_non_alphanumeric(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

# Applying the function to the 'text' column to create 'cleaned_text'
df['cleaned_text'] = df['text'].apply(remove_non_alphanumeric)

#Visualization


#distribution of target variable
plt.figure(figsize=(6, 4))
sns.countplot(x='target', data=df, palette='viridis')
plt.title('Distribution of Target Variable')
plt.xlabel('Target')
plt.ylabel('Count')
plt.show()

#bar plot of top 10 keywords
top_keywords = df['keyword'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_keywords.index, y=top_keywords.values, palette='coolwarm')
plt.title('Top 10 Keywords')
plt.xlabel('Keyword')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

#bar plot of top 10 locations
top_locations = df['location'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_locations.index, y=top_locations.values, palette='magma')
plt.title('Top 10 Locations')
plt.xlabel('Location')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

#Word Cloud for 'text' column
text_data = ' '.join(df['cleaned_text'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Cleaned Text')
plt.show()
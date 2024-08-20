import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import plotly.express as px

# Load the dataset
df = pd.read_csv('/content/apps.csv')

df=df.drop('Unnamed: 0',axis=1)
df=df.drop('Current Ver',axis=1)
df=df.drop('Android Ver',axis=1)

df.isnull().sum()
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())
df['Size'] = df['Size'].fillna(df['Size'].mean())

df.info()

# Data Preparation
df = df.drop_duplicates()
df = df.dropna(subset=['Rating', 'Category'])
df['Rating'] = df['Rating'].astype(float)
df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)

# Category Exploration
category_counts = df['Category'].value_counts()
print(category_counts)

from tkinter import font
# Metrics Analysis
plt.figure(figsize=(8, 6))
sns.barplot(x=category_counts.index, y=category_counts.values, palette='plasma')
plt.title('Category Exploration')
plt.xlabel('Category')
plt.ylabel('Number of Apps')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df['Rating'], bins=50, kde=True, color='purple',alpha=0.3)
plt.title('Distribution of App Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Category', y='Size', data=df, palette='viridis')
plt.title('App Size Distribution by Category')
plt.xlabel('Category')
plt.ylabel('Size MB')
plt.xticks(rotation=90)
plt.show()
print()
print("The box plot visualizes the distribution of app sizes (in MB) across various categories.")

plt.figure(figsize=(8, 6))
sns.lineplot(x='Category', y='Price', data=df, marker='o', color='green')
plt.title('Pricing Trends')
plt.xlabel('Category')
plt.ylabel('Price (USD)')
plt.xticks(rotation=90)
plt.show()

df2 = pd.read_csv('/content/user_reviews.csv')
df2['Sentiment'] = df2['Sentiment'].fillna("Neutral")
df2['Sentiment'] = df2['Sentiment_Polarity'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
plt.figure(figsize=(5, 5))
sns.countplot(x='Sentiment', data=df2, palette='plasma', width=0.5,alpha=0.5)
plt.title('Distribution of Sentiments')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

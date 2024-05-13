import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

# Read data from csv file
df = pd.read_csv('tweets.csv')

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    if text and isinstance(text, str):
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity
        return pd.Series([polarity, subjectivity], index=['polarity', 'subjectivity'])
    else:
        return pd.Series([0, 0], index=['polarity', 'subjectivity'])

# Apply sentiment analysis to the text column
df[['polarity', 'subjectivity']] = df['text'].apply(analyze_sentiment)

# Create sentiment column based on polarity
df['sentiment'] = df['polarity'].apply(lambda x: 1 if x > 0 else 0)

# Visualization
sns.set(style='whitegrid')
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(data=df, x='sentiment', kde=True, color='b')
ax.set_title('Sentiment Analysis of Tweets')
ax.set_xlabel('Sentiment (1=Positive, 0=Negative)')
ax.set_ylabel('Frequency')
plt.show()

# Output the result in the required format
print(df.to_markdown(index=False))